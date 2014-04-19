# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class FinalType(AbsObj):
    '''
        Тип страховки игрока
    '''

    class Meta:
        app_label           = "grizzly"
        verbose_name        = "Игра: матч: тип финала"
        verbose_name_plural = "Играы: матчы: типы финала"
