# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj


class GameMatch (AbsGameObj):

    rink = models.ForeignKey(
        'Rink',
        blank=True,
        null=True,
        verbose_name=u"каток"
    )

    team_a = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда A",
        related_name="team_a",
    )

    team_b = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда Б",
        related_name="team_b",
    )

    score_a = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"счет A"
    )

    score_b = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"счет Б"
    )

    judges = models.ManyToManyField(
        'Judge',
        blank=True,
        null=True,
        verbose_name=u"судьи"
    )



    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч"
        verbose_name_plural = "Игры: матчи"
