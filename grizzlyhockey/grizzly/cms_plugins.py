# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from grizzly.models import GrizzlyPlugin as GrizzlyPluginModel
from grizzly.models import TeamPlugin as TeamPluginModel

from grizzly.models import GameSeasonPlugin as GameSeasonPluginModel

from django.utils.translation import ugettext as _



class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel  #
    name = _("Grizzly Team Plugin") #
    render_template = "grizzly/plugins/team.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameSeasonPlugin(CMSPluginBase):
    model = GameSeasonPluginModel  #
    name = _("Grizzly GameSeason Plugin") #
    render_template = "grizzly/plugins/gameseason.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


plugin_pool.register_plugin(TeamPlugin) # register the plugin

plugin_pool.register_plugin(GameSeasonPlugin) # register the plugin

