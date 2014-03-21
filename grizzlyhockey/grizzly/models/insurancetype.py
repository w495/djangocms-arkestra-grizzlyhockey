# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class InsuranceType(AbsObj):
    '''
        Тип страховки игрока
    '''

    class Meta:
        app_label           = "grizzly"
        verbose_name        = "тип страховки игрока"
        verbose_name_plural = "игроки: типы страховок"
