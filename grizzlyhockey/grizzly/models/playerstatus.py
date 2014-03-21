# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class PlayerStatus(AbsObj):
    '''
        Статус игрока
    '''

    class Meta:
        app_label    = "grizzly"
        verbose_name = "статус игрока"
        verbose_name_plural = "игроки: статусы игроков"
