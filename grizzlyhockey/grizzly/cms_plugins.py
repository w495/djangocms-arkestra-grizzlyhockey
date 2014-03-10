from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from grizzly.models import GrizzlyPlugin as GrizzlyPluginModel
from grizzly.models import PlayerPlugin as PlayerPluginModel


from django.utils.translation import ugettext as _

class GrizzlyPlugin(CMSPluginBase):
    model = GrizzlyPluginModel # Model where data about this plugin is saved
    name = _("Grizzly Plugin") # Name of the plugin
    render_template = "grizzly/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class PlayerPlugin(CMSPluginBase):
    model = PlayerPluginModel # Model where data about this plugin is saved
    name = _("Grizzly Player Plugin") # Name of the plugin
    render_template = "grizzly/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


plugin_pool.register_plugin(PlayerPlugin) # register the plugin

plugin_pool.register_plugin(GrizzlyPlugin) # register the plugin

