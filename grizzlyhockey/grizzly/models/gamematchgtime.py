# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameMatchGTime (AbsObj):


    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )

    time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время"
    )

    a = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"А"
    )


    b = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"Б"
    )



    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игра: матч: время игры вратарей"
        verbose_name_plural = "Игры: матчи: время игры вратарей"
