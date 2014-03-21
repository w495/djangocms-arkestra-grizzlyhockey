# -*- coding: utf-8 -*-

from django.db import models

from absplugin import AbsPlugin


class PlayerPlugin(AbsPlugin):
    '''
        Плагин для отображения игрок в поле расширенного текста
    '''

    player = models.ForeignKey(
        'Player',
        verbose_name=u"игрок"
    )

    class Meta:
        app_label = "grizzly"
        verbose_name = "Гризли плагин: игрок"
        verbose_name_plural = "Гризли плагин: игрок"
