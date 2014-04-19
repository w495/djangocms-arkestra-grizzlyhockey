# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj

class GameTournamentPlayOff (AbsGameObj):
    '''

        create table grizzly_gametournamentplayoff like grizzly_gametournamentregular;

    '''
    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )


    def get_tours(self):
        all_team = self.teams.all().count()
        if (all_team % 2):
            all_team += 1;
        return range(1, all_team )



    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: турнир play-off"
        verbose_name_plural = "Игры: турниры play-off"
