# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers
from absobj import AbsObj

class Player2Team(AbsObj):

    status = models.ForeignKey(
        'PlayerStatus',
        blank = True,
        null = True,
        verbose_name = u"статус"
    )

    game_number = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )

    role = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"амплуа"
    )

    team = models.ForeignKey(
        'Team',
        blank = True,
        null = True,
        verbose_name = u"команда"
    )

    player = models.ForeignKey(
        'Player',
        blank = True,
        null = True,
        verbose_name = u"игрок"
    )


    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока: команду"
        verbose_name_plural = "игроки: команды"
