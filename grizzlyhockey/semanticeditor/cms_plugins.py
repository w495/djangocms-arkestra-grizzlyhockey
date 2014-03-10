from cms.models import Page
from cms.plugins.text.cms_plugins import TextPlugin
from cms.plugins.text.models import Text
from cms.plugins.text.forms import TextForm
from cms.plugins.text.utils import plugin_tags_to_user_html
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _

from semanticeditor.widgets import SemanticEditor
from django.forms.fields import CharField

import re

class SemanticTextPlugin(TextPlugin):

    name = _("Text/layout")
    admin_preview = False

    # A lot of duplication from TextPlugin because get_form needs to find out
    # what page/template we are using, and pass that on to get_editor_widget

    def get_editor_widget(self, request, plugins, page):
        return SemanticEditor(installed_plugins=plugins,
                              page=page)

    def get_form_class(self, request, plugins, page):
        """
        Returns a subclass of Form to be used by this plugin
        """
        # We avoid mutating the Form declared above by subclassing
        class TextPluginForm(self.form):
            pass

        widget = self.get_editor_widget(request, plugins, page)
        TextPluginForm.declared_fields["body"] = CharField(widget=widget, required=False)
        return TextPluginForm

    def get_form(self, request, obj=None, **kwargs):

        page = None
        # In theory, placeholders can belong to many pages. In practice
        # they usually belong to just one.
        try:
            page = self.placeholder.page_set.all()[0]
        except IndexError:
            pass

        if page is None and obj is not None:
            # Fallback for Arkestra:
             placeholder = obj.placeholder
             field = placeholder._get_attached_field_name()
             model = placeholder._get_attached_model()

             # all Arkestra models with placeholders will (should) have a
             # get_website property.
             try:
                 page = model.objects.get(**{field: placeholder.id}).get_website    
             # older Arkestra versions used a get_website() method
             except TypeError:
                 page = model.objects.get(**{field: placeholder.id}).get_website()    
             except AttributeError:
                 pass

        if page is None:
            import warnings
            warnings.warn("Couldn't work out page for this item, which will result in problems with CSS class list")

        plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, page)
        form = self.get_form_class(request, plugins, page)
        kwargs['form'] = form # override standard form
        return super(TextPlugin, self).get_form(request, obj, **kwargs)

plugin_pool.register_plugin(SemanticTextPlugin)
