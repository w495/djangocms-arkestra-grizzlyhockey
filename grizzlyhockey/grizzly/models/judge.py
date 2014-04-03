# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers
from gamematch import GameMatch

class Judge(AbsPers):

    types = models.ManyToManyField(
        'JudgeType',
        blank=True,
        null=True,
        verbose_name=u"что судит"
    )

    gamematches = models.ManyToManyField(
        'GameMatch',
        blank=True,
        null=True,
        through=GameMatch.judges.through,
        verbose_name=u"матчи"
    )

    class Meta:
        app_label = "grizzly"
        verbose_name = "судьи"
        verbose_name_plural = "судьи"

