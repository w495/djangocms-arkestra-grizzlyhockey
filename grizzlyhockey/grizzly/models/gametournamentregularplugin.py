# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin

class GameTournamentRegularPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    gametournamentregular = models.ForeignKey(
        'GameDivision',
        verbose_name=u"GameTournamentRegular"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: турнир регулярный"
        verbose_name_plural = "Игры: турниры регулярные"
