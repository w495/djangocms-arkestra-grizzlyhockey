# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin


class GameMatchPluginMany(AbsPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    gamematchs = models.ManyToManyField(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"матчи"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: матчи"
        verbose_name_plural = "Гризли плагин: матчи"
