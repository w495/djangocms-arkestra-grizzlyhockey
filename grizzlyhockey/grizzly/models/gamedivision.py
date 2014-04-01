# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj
from team import Team
from gameseason import GameSeason

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

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: дивизион"
        verbose_name_plural = "Игры: дивизионы"
