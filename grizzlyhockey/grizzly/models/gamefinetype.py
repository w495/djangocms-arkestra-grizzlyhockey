# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameFineType (AbsObj):

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: штрафы: типы"
        verbose_name_plural = "Игры: матчи: штрафы: типы"
