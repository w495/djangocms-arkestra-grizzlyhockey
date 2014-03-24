# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin
from cms.models import CMSPlugin


class GameMatchPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gamematch = models.ForeignKey(
        'GameMatch',
        verbose_name=u"матч"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = u"Гризли плагин: матч"
        verbose_name_plural = u"Гризли плагин: матч"

