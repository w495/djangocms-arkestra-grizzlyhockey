# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin

class GameSeasonPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gameseason = models.ForeignKey(
        'GameSeason',
        blank=True,
        null=True,
        verbose_name=u"игровой сезон"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: игровой сезон"
        verbose_name_plural = "Гризли плагин: игровой сезон"

