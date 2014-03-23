# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameMatchPenalty (AbsObj):

    a = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )


    b = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )

    gla = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )

    glb = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )


    result = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )


    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: штрафные броски после игры"
        verbose_name_plural = "Игры: матчи: штрафные броски после игры"
