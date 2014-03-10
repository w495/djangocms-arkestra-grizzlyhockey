from cms.plugins.text import settings as text_settings
from cms.plugins.text.widgets.wymeditor_widget  import WYMEditor
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language
import os

join = os.path.join

class SemanticEditor(WYMEditor):

    class Media:
        js = [join(settings.SEMANTICEDITOR_MEDIA_URL, path) for path in
              ('javascript/wymeditor/plugins/semantic/wymeditor.semantic.js',
               'javascript/json2.js',
               'javascript/jquery.query-2.1.7.js',
               )]

    def __init__(self, attrs=None, installed_plugins=None, page=None):
        self.page = page
        super(SemanticEditor, self).__init__(attrs=attrs, installed_plugins=installed_plugins)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
        containers = getattr(settings, 'WYM_CONTAINERS', None)
        if containers is None:
            containers = text_settings.WYM_CONTAINERS
        context = {
            'name': name,
            'language': language,
            'SEMANTICEDITOR_MEDIA_URL': settings.SEMANTICEDITOR_MEDIA_URL,
            'CMS_MEDIA_URL': settings.CMS_MEDIA_URL,
            'WYM_TOOLS': mark_safe(text_settings.WYM_TOOLS),
            'WYM_CONTAINERS': mark_safe(containers),
            'WYM_CLASSES': mark_safe(text_settings.WYM_CLASSES),
            'WYM_STYLES': mark_safe(text_settings.WYM_STYLES),
            'WYM_STYLESHEET': mark_safe(text_settings.WYM_STYLESHEET),
            'installed_plugins': self.installed_plugins,
            'page': self.page,
        }

        return mark_safe(render_to_string(
            'semanticeditor/editorwidget.html', context))
