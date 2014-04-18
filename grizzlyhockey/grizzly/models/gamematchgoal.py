# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj
import time



class GameMatchGoal (AbsObj):
    '''

        from grizzly.models import GameMatchGoal
        [p.resave() for p in GameMatchGoal.objects.all()]


    '''
    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )

    #alter table  grizzly_gamematchgoal add `minute` int(11) default null;
    #update grizzly_gamematchgoal ste minute = minute(time);
    minute = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Минута"
    )

    #alter table  grizzly_gamematchgoal add `second` int(11) default null;
    #update grizzly_gamematchgoal set second = second(time);
    second = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Секунда"
    )

    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда",
    )

    goalno = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"номер шайбы"
    )


    #alter table  grizzly_gamematchgoal add `goal_keeper_id` int(11) default null;
    ##
    ## Игрок, вратарь
    ##
    goal_keeper = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"вратарь",
        related_name="gamematchgoal_miss"
    )


    ##
    ## Игрок, забросивший шайбу
    ##
    goal_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игрок, забросивший шайбу",
        related_name="gamematchgoal_goal"
    )

    ##
    ## Игроки, сделавшие результативную передачу
    ##
    trans_players = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки, сделавшие результативную передачу"
    )

    game_situation = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровая ситуация"
    )

    def pre_save_action(self, *args, **kwargs):

        gtimes = [
            gtime
            for gtime in self.gamematch.gamematchgtime_set.filter(
                start_minute__lt = self.minute,
                stop_minute__gt = self.minute,
            ).exclude(team = self.team)
        ]

        if gtimes:
            self.goal_keeper = gtimes[0].player


    def async_save_action(self, *args, **kwargs):
        if(self.team):
            self.team.async_resave()

        if(self.goal_player):
            self.goal_player.resave_player2team_set()

        if(self.goal_keeper):
            self.goal_keeper.resave_player2team_set()

        [p.resave_player2team_set() for p in self.trans_players.all()]





    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: гол"
        verbose_name_plural = "Игры: матчи: голы"
