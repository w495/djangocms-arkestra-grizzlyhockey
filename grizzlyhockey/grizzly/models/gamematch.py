# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj


class GameMatch (AbsGameObj):

    rink = models.ForeignKey(
        'Rink',
        blank=True,
        null=True,
        verbose_name=u"каток"
    )

    team_a = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда A",
        related_name="team_a",
    )

    team_b = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда Б",
        related_name="team_b",
    )

    score_a = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"счет A"
    )

    score_b = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"счет Б"
    )

    judges = models.ManyToManyField(
        'Judge',
        blank=True,
        null=True,
        verbose_name=u"судьи"
    )


    gametournamentregular = models.ForeignKey(
        'GameTournamentRegular',
        blank=True,
        null=True,
        verbose_name=u"Турнир"
    )


    def __str__(self):
        rink = ""
        if(self.rink):
            rink = "(%s)"%self.rink
        team_a = ""
        if(self.team_a):
            team_a = "«%s»"%self.team_a.name

        team_b = ""
        if(self.team_b):
            team_b = "«%s»"%self.team_b.name

        return u"%s (%s): «%s» × «%s»"%(self.name, rink, team_a, team_b)

    def __unicode__(self):
        return self.__str__()


    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч"
        verbose_name_plural = "Игры: матчи"
