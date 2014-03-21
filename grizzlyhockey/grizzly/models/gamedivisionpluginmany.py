# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin


class GameDivisionPluginMany(AbsPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: дивизионы"
        verbose_name_plural = "Гризли плагин: дивизионы"
