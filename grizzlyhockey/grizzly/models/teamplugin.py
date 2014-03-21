# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin


class TeamPlugin(AbsPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    team = models.ForeignKey(
        'Team',
        verbose_name=u"команда"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: команда"
        verbose_name_plural = "Гризли плагин: команды"
