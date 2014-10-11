# -*- coding: utf-8 -*-
import logging

from django.db import models
from absgameobj import AbsGameObj
from gamematchgtime import GameMatchGTime
from gamematchgoal import GameMatchGoal

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
        related_name="gamematch_a",
    )

    team_b = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда Б",
        related_name="gamematch_b",
    )

    players_a = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки А",
        related_name="gamematch_a"
    )

    players_b = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки Б",
        related_name="gamematch_b"
    )

    best_player_a = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"лучший игрок команды A",
        related_name="best_player_a"
    )

    best_player_b = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"лучший игрок команды Б",
        related_name="best_player_b"
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

    tourno = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"тур"
    )


    # alter table grizzly_gamematch add `finaltype_id` int(11) default null;

    finaltype = models.ForeignKey(
        'FinalType',
        blank=True,
        null=True,
        verbose_name = u"финал"
    )


    gametournamentregular = models.ForeignKey(
        'GameTournamentRegular',
        blank=True,
        null=True,
        verbose_name=u"Турнир регулярный"
    )


    # alter table grizzly_gamematch add `gametournamentplayoff_id` int(11) DEFAULT NULL;

    gametournamentplayoff = models.ForeignKey(
        'GameTournamentPlayOff',
        blank=True,
        null=True,
        verbose_name=u"Турнир play оff"
    )
    
    def pre_save_action(self):
        [ goal.resave() for goal in GameMatchGoal.objects.filter(gamematch = self) ]
    
    def async_save_action(self):
        [ gtime.resave() for gtime in GameMatchGTime.objects.filter(gamematch = self) ]
        self.team_a.resave()
        self.team_b.resave()


    class Meta:
        ordering = ['ctime',]
        app_label = "grizzly"
        verbose_name = "Игры: матч"
        verbose_name_plural = "Игры: матчи"

