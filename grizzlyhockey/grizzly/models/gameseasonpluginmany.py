# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin

class GameSeasonPluginMany(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''
    
    gameseasons = models.ManyToManyField(
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

