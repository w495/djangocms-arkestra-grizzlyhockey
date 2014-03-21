# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin


class TeamPluginMany(AbsPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: команды"
        verbose_name_plural = "Гризли плагин: команды"

