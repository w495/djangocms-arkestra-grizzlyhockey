# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj

class GameSeason (AbsGameObj):

    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: сезон"
        verbose_name_plural = "Игры: сезоны"