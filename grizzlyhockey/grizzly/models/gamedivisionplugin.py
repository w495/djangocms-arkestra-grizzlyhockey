# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin
from cms.models import CMSPlugin


class GameDivisionPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gamedivision = models.ForeignKey(
        'GameDivision',
        verbose_name=u"игровой дивизион"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = u"Гризли плагин: дивизион"
        verbose_name_plural = u"Гризли плагин: дивизион"

