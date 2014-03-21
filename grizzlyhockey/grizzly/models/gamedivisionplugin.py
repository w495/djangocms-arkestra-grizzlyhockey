# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin


class GameDivisionPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gamedivision = models.ForeignKey(
        'GameDivision',
        verbose_name=u"игровой дивизион"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: дивизион"
        verbose_name_plural = "Гризли плагин: дивизион"

