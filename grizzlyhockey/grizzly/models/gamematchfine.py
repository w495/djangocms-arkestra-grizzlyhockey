# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameMatchFine (AbsObj):

    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )

    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда",
        related_name="team",
    )

    ##
    ## Фактическое начало отбывания наказания
    ##
    start_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время"
    )

    ##
    ## Фактическое окончание штрафного времени
    ##
    stop_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время"
    )

    ##
    ## Игрок,
    ##
    fine_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"тренер"
    )

    ##
    ## Тип нарушения
    ##
    type = models.ForeignKey(
        'GameFineType',
        blank=True,
        null=True,
        verbose_name=u"тип"
    )


    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игра: матч: штраф"
        verbose_name_plural = "Игры: матчи: штрафы"
