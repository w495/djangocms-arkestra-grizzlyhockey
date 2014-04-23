# -*- coding: utf-8 -*-

import operator
import datetime

from django.db.models import Q

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from grizzly.models import PlayerPlugin as PlayerPluginModel
from grizzly.models import TeamPlugin as TeamPluginModel
from grizzly.models import TeamPluginMany as TeamPluginManyModel

from grizzly.models import GameSeasonPlugin     as GameSeasonPluginModel
from grizzly.models import GameSeasonPluginMany as GameSeasonPluginManyModel

from grizzly.models import GameDivisionPlugin       as GameDivisionPluginModel
from grizzly.models import GameDivisionPluginMany   as GameDivisionPluginManyModel

from grizzly.models import GameTournamentRegularPlugin       as GameTournamentRegularPluginModel
from grizzly.models import GameTournamentRegularPluginMany   as GameTournamentRegularPluginManyModel

from grizzly.models import GameMatchPlugin      as GameMatchPluginModel
from grizzly.models import GameMatchPluginMany  as GameMatchPluginManyModel

from grizzly.models import GameMatch

from grizzly.models import Player



from django.utils.translation import ugettext as _


class TeamPluginMany(CMSPluginBase):
    model = TeamPluginManyModel
    name = _(u"Гризли: несколько команд")
    render_template = "grizzly/plugins/teammany.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel  #
    name = _(u"Гризли: команда") #
    render_template = "grizzly/plugins/team.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



class PlayerPlugin(CMSPluginBase):
    model = PlayerPluginModel  #
    name = _(u"Гризли: игрок") #
    render_template = "grizzly/plugins/player.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameSeasonPlugin(CMSPluginBase):
    model = GameSeasonPluginModel  #
    name = _(u"Гризли: сезон") #
    render_template = "grizzly/plugins/gameseason.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameDivisionPlugin(CMSPluginBase):
    model = GameDivisionPluginModel  #
    name = _(u"Гризли: дивизион") #
    render_template = "grizzly/plugins/gamedivision.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameDivisionPluginMany(CMSPluginBase):
    model = GameDivisionPluginManyModel  #
    name = _(u"Гризли: несколько дивизионов") #
    render_template = "grizzly/plugins/gamedivisionmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameTournamentRegularPlugin(CMSPluginBase):
    model = GameTournamentRegularPluginModel  #
    name = _(u"Гризли: регулярный чемпионат") #
    render_template = "grizzly/plugins/gametournamentregular.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameTournamentRegularPluginMany(CMSPluginBase):
    model = GameTournamentRegularPluginManyModel  #
    name = _(u"Гризли: несколько регулярных чемпионатов") #
    render_template = "grizzly/plugins/gametournamentregularmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameMatchPluginMany(CMSPluginBase):
    model = GameMatchPluginManyModel  #
    name = _(u"Гризли: несколько матчей") #
    render_template = "grizzly/plugins/gamematchmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameMatchPlugin(CMSPluginBase):
    model = GameMatchPluginModel  #
    name = _(u"Гризли: матч") #
    render_template = "grizzly/plugins/gamematch.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameMatchSchedulePlugin(CMSPluginBase):
    name = _(u"Гризли: расписание матчей") #
    render_template = "grizzly/plugins/gamematchschedule.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

    def render(self, context, instance, placeholder):

        date = datetime.date.today()
        end_week = date + datetime.timedelta(10)
        gamematches =  GameMatch.objects.filter(
            start_datetime__range = [date, end_week]
        ).order_by('start_datetime')

        instance.gamematches = gamematches
        context['instance'] = instance
        return context


class PlayerBirthdayPlugin(CMSPluginBase):
    name = _(u"Гризли: Дни рождения") #
    render_template = "grizzly/plugins/playerbirthday.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

    def render(self, context, instance, placeholder):
        players =  self.birthdays_within()
        instance.players = players
        context['instance'] = instance
        return context

    def birthdays_within(self, days = 1):

        date = datetime.datetime.now()

        now = date - datetime.timedelta(days=0)
        then = date + datetime.timedelta(days=days)

        # Build the list of month/day tuples.
        monthdays = [(now.month, now.day)]
        while now <= then:
            monthdays.append((now.month, now.day))
            now += datetime.timedelta(days=1)

        # Tranform each into queryset keyword args.
        monthdays = (dict(zip(("birthday__month", "birthday__day"), t))
                    for t in monthdays)

        # Compose the djano.db.models.Q objects together for a single query.
        query = reduce(operator.or_, (Q(**d) for d in monthdays))

        # Run the query.

        players = [player for player in Player.objects.filter(query)]

        players = sorted(players, key = lambda x: x.birthday.month * 100 +  x.birthday.day)

        return players


plugin_pool.register_plugin(PlayerBirthdayPlugin)
plugin_pool.register_plugin(TeamPlugin)
plugin_pool.register_plugin(TeamPluginMany)
plugin_pool.register_plugin(PlayerPlugin)

plugin_pool.register_plugin(GameSeasonPlugin)

plugin_pool.register_plugin(GameDivisionPlugin)
plugin_pool.register_plugin(GameDivisionPluginMany)

plugin_pool.register_plugin(GameTournamentRegularPlugin)
plugin_pool.register_plugin(GameTournamentRegularPluginMany)

plugin_pool.register_plugin(GameMatchPlugin)

plugin_pool.register_plugin(GameMatchSchedulePlugin)

plugin_pool.register_plugin(GameMatchPluginMany)

