# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj
from player import Player


class Team(AbsObj):

    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"дата создания"
    )

    players = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        through=Player.teams.through,
        verbose_name=u"игроки"
    )

    teamschedules = models.ManyToManyField(
        'TeamSchedule',
        blank=True,
        null=True,
        verbose_name=u"расписания"
    )

    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "команду"
        verbose_name_plural = "команды"
