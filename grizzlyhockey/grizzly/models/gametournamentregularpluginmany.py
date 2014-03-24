# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin

class GameTournamentRegularPluginMany(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gametournamentregulars = models.ManyToManyField(
        'GameTournamentRegular',
        blank=True,
        null=True,
        verbose_name=u"турнир регулярный"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Гризли плагин: турнир регулярный"
        verbose_name_plural = "Гризли плагин: турниры регулярные"
