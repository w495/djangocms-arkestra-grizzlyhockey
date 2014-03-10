from cms.models import Page
from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import mail_admins
from django.conf import settings
from django.utils.translation import ugettext as _
from semanticeditor.api import extract_presentation, format_html, preview_html, AllUserErrors, COMMANDS, PresentationInfo, PresentationClass, clean_html, get_classes
from semanticeditor.models import CssClass
import sys
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.3, 2.4 fallback.

# in django CMS 2.4, settings.CMS_TEMPLATE_INHERITANCE_MAGIC is unavailable
try:
    TEMPLATE_INHERITANCE_MAGIC = settings.CMS_TEMPLATE_INHERITANCE_MAGIC
except AttributeError:
    import cms.constants
    TEMPLATE_INHERITANCE_MAGIC = cms.constants.TEMPLATE_INHERITANCE_MAGIC


def json_view(func):
    """
    Use this decorator on a function that takes a request and returns
    a dictionary of values in order to create a view that handles
    errors and return JSON.

    The dictionary should be in this standard format:

    {'result': 'ok',
     'value': your_actual_value
    }

    or

    {'result': 'usererror',
     'message': an_error_message

    or

    {'result': 'error',
     'message': an_error_message
    }
    """
    def wrapper(request, *a, **kw):
        response = None
        try:
            response = func(request, *a, **kw)
        except Exception, e:
            # Mail the admins with the error
            exc_info = sys.exc_info()
            subject = 'JSON view error: %s' % request.path
            try:
                request_repr = repr(request)
            except:
                request_repr = 'Request repr() unavailable'
            import traceback
            message = 'Traceback:\n%s\n\nRequest:\n%s' % (
                '\n'.join(traceback.format_exception(*exc_info)),
                request_repr,
                )
            mail_admins(subject, message, fail_silently=True)

            # Come what may, we're returning JSON.
            if hasattr(e, 'message'):
                msg = e.message
            else:
                msg = _('Internal error')+': '+ str(e)
            response = error(msg)

        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='application/json')

    return wraps(func)(wrapper)


def error(msg):
    """
    Standard error result - for internal errors
    """
    return dict(result='error', message=msg)


def failure(msg):
    """
    Standard failure result
    """
    return dict(result='usererror', message=msg)


def success(value):
    """
    Standard success result
    """
    return dict(result='ok', value=value)


# Anything that depends on values the user may have entered and might
# contain 'errors' should use this, normally passing in AllUserErrors
# as 'exceptions'.  'server' errors are handled by @json_view
def graceful_errors(exceptions, callback):
    """
    Retrieve a value from a callback, handling the exceptions that
    are passed in, and returning in standard formats
    """
    try:
        val = callback()
    except exceptions, e:
        return failure(e.args[0])
    return success(val)


def PI_to_dict(pi):
    """
    Converts a PresentationInfo to a dictionary
    for use client side
    """
    d = {}
    # We need to filter out things that are server side only and can't be
    # turned into JSON.
    allowed = set([str, unicode, int, bool, dict, list])
    for k, v in pi.__dict__.items():
        if type(v) in allowed:
            d[k] = v
    return d


def dict_to_PI(d, classes):
    """
    Convert a dictionary to a PresentationInfo,
    using a pre-fetched dictionary of CssClass objects
    """
    if d['prestype'] == 'command':
        return PresentationInfo(prestype=d['prestype'], name=d['name'])
    else:
        c = classes.get(d['name'])
        if c is None:
            return None
        else:
            return css_class_to_presentation_class(c)


def css_class_to_presentation_class(c):
    return PresentationClass(c.name,
                             verbose_name=c.verbose_name,
                             description=c.description,
                             allowed_elements=c.allowed_elements.lower().split(' '),
                             column_equiv=c.column_equiv,
                             category=c.category.name if c.category is not None else None)


@json_view
def retrieve_styles(request):
    template = request.GET['template']
    page_id = request.GET['page_id']
    if template == TEMPLATE_INHERITANCE_MAGIC:
        # Need to look up page to find out what template to use
        p = Page.objects.get(pk=page_id)
        template = p.get_template()
    classes = get_classes(template)
    retval = map(css_class_to_presentation_class,
                 classes)
    return success(map(PI_to_dict,retval))


@json_view
def retrieve_commands(request):
    return success(map(PI_to_dict, COMMANDS))


@json_view
def separate_presentation(request):
    """
    Returns a JSON object:
     { presentation: <dictionary of presentation info from html>
       html: <input html stripped of presentation>
     }
    """
    data = request.POST.get('html','')

    def _handled():
        pres, html = extract_presentation(data)
        # Rewrite pres so that we can serialise it to JSON
        pres2 = {}
        for k, v in pres.items():
            pres2[k] = [PI_to_dict(p) for p in v]
        return dict(presentation=pres2,
                    html=html)

    return graceful_errors(AllUserErrors, _handled)


def _convert_pres(pres):
    # Convert dictionaries into PresentationInfo classes. We need actual
    # CssClass instances in order to be able to restore column_equiv and
    # allowed_elements info
    classes = dict((c.name, c) for c in CssClass.objects.all())
    retval = {}
    for k, v in pres.items():
        # v is list of PI dicts
        newlist = []
        for i, item in enumerate(v):
            pi = dict_to_PI(item, classes)
            # if CssClass was removed from DB, pi can be None
            if pi is not None:
                newlist.append(pi)
        retval[k]= newlist
    return retval


@json_view
def combine_presentation(request):
    """
    Combines submitted 'html' and 'presentation' data,
    returning a dictionary containing { html: <combined html> }
    """
    html = request.POST.get('html', '')
    presentation = request.POST.get('presentation', '{}')
    presentation = simplejson.loads(presentation)
    presentation = _convert_pres(presentation)
    return graceful_errors(AllUserErrors, lambda: dict(html=format_html(html, presentation, pretty_print=True)))


@json_view
def preview(request):
    html = request.POST.get('html', '')
    presentation = request.POST.get('presentation', '{}')
    presentation = simplejson.loads(presentation)
    presentation = _convert_pres(presentation)

    return graceful_errors(AllUserErrors, lambda: dict(html=preview_html(html, presentation)))


@json_view
def clean_html_view(request):
    html = request.POST.get('html', '')
    return graceful_errors(AllUserErrors, lambda: dict(html=clean_html(html)))
