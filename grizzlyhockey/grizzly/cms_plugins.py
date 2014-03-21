# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from grizzly.models import PlayerPlugin as PlayerPluginModel
from grizzly.models import TeamPlugin as TeamPluginModel
from grizzly.models import TeamPluginMany as TeamPluginManyModel

from grizzly.models import GameSeasonPlugin as GameSeasonPluginModel
from grizzly.models import GameDivisionPluginMany as GameDivisionPluginManyModel

from grizzly.models import GameDivisionPlugin as GameDivisionPluginModel


from django.utils.translation import ugettext as _


class TeamPluginMany(CMSPluginBase):
    model = TeamPluginManyModel
    name = _("Grizzly Teams Many Plugin")
    render_template = "grizzly/plugins/teammany.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel  #
    name = _("Grizzly Team Plugin") #
    render_template = "grizzly/plugins/team.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



class PlayerPlugin(CMSPluginBase):
    model = PlayerPluginModel  #
    name = _("Grizzly Player Plugin") #
    render_template = "grizzly/plugins/player.html" # template to render the plugin with
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

class GameDivisionPluginMany(CMSPluginBase):
    model = GameDivisionPluginManyModel  #
    name = _("Grizzly GameDivision Many Plugin") #
    render_template = "grizzly/plugins/gamedivisionmanyplugin.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameDivisionPlugin(CMSPluginBase):
    model = GameDivisionPluginModel  #
    name = _("Grizzly GameDivision Plugin") #
    render_template = "grizzly/plugins/gamedivision.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


plugin_pool.register_plugin(TeamPluginMany)

plugin_pool.register_plugin(TeamPlugin)

plugin_pool.register_plugin(PlayerPlugin)

plugin_pool.register_plugin(GameSeasonPlugin)


plugin_pool.register_plugin(GameDivisionPluginMany)

plugin_pool.register_plugin(GameDivisionPlugin)
