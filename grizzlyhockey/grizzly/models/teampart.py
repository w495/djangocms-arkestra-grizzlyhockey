# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class TeamPart(AbsObj):

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    players = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "составы команд"
        verbose_name_plural = "составы команд"
