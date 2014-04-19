# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj
from team import Team
from gameseason import GameSeason

from gametournamentregular import GameTournamentRegular
from player2team import Player2Team


class GameDivision(AbsGameObj):

    gameseasons = models.ManyToManyField(
        'GameSeason',
        blank=True,
        null=True,
        through=GameSeason.gamedivisions.through,
        verbose_name=u"сезоны"
    )

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        through=Team.gamedivisions.through,
        verbose_name=u"команды"
    )

    gametournamentregulars = models.ManyToManyField(
        'GameTournamentRegular',
        blank=True,
        null=True,
        through=GameTournamentRegular.gamedivisions.through,
        verbose_name=u"регулярные чемпионаты"
    )


    def get_some_p2t(self, *args):
        teams = [team for team  in self.teams.all()]
        objs = [x for x in Player2Team.objects.filter(team__in = teams).order_by(*args)]
        return objs

    def get_p2t(self):
        objs = self.get_some_p2t('-ngoalsntrans')
        return objs

    def get_max_some_p2t(self, *args):
        objs = self.get_some_p2t(*args)
        if(objs):
            return objs[0]
        return None

    def get_max_ngoalsntrans_p2t(self):
        return self.get_max_some_p2t('-ngoalsntrans')

    def get_max_ngoals_p2t(self):
        return self.get_max_some_p2t('-ngoals')

    def get_max_ntrans_p2t(self):
        return self.get_max_some_p2t('-ntrans')

    def get_min_nmisses_p2t(self):
         return self.get_max_some_p2t('nmisses')


    def get_max_safety_factor_p2t(self):
         return self.get_max_some_p2t('-safety_factor')







    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: дивизион"
        verbose_name_plural = "Игры: дивизионы"
