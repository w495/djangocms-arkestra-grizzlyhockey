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
    #update grizzly_gamematchgoal set minute = minute(time);
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
    
    ##
    ## Игроки, сделавшие результативную передачу
    ##
    assistant_1 = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"ассистент 1",
        related_name="gamematchgoal_assistant_1"
    )
    
    ##
    ## Игроки, сделавшие результативную передачу
    ##
    assistant_2 = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"ассистент 2",
        related_name="gamematchgoal_assistant_2"
    )
    
    ##
    ## Игроки команды А, находившиеся на площадке
    ##
    rink_players_a = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки команды A на площадке",
        related_name="gamematchgoal_rink_players_a"
    )
    
    ##
    ## Игроки команды Б, находившиеся на площадке
    ##
    rink_players_b = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки команды B на площадке",
        related_name="gamematchgoal_rink_players_b"
    )
    
    game_situation = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровая ситуация"
    )
    
    #  alter table grizzly_gamematchgoal add is_power_play bool default 0;
    is_power_play = models.BooleanField(
        default=False,
        verbose_name = u'гол в большинстве'
    )
    
    #  alter table grizzly_gamematchgoal add is_short_handed bool default 0;
    is_short_handed = models.BooleanField(
        default=False,
        verbose_name = u'гол в меньшинстве'
    )
    
    #  alter table grizzly_gamematchgoal add is_win_goal bool default 0;
    is_win_goal = models.BooleanField(
        default=False,
        verbose_name = u'победный гол'
    )
    
    def resave_goalkeeper(self, *args, **kwargs):
        for gtime in self.gamematch.gamematchgtime_set.all():
            gtime.save()
        if self.goal_keeper:
            #print self.goal_keeper.first_name
            #print self.goal_keeper.second_name
            self.goal_keeper.resave_player2team_set()
        else:
            if(self.team):
                gtimes = [
                    gtime
                    for gtime in self.gamematch.gamematchgtime_set.filter(
                        start_minute__lt = self.minute+1,
                        stop_minute__gte = self.minute+1,
                    ).exclude(team = self.team)
                ]
            else:
                gtimes = [
                    gtime
                    for gtime in self.gamematch.gamematchgtime_set.filter(
                        start_minute__lt = self.minute+1,
                        stop_minute__gte = self.minute+1,
                    )
                ]
            if gtimes:
                self.goal_keeper = gtimes[0].player
                self.goal_keeper.resave_player2team_set()
                self.save()
    
    def pre_save_action(self, *args, **kwargs):
        if(self.minute):
            if(self.team):
                gtimes = [
                    gtime
                    for gtime in self.gamematch.gamematchgtime_set.filter(
                        start_minute__lt = self.minute,
                        stop_minute__gte = self.minute,
                    ).exclude(team = self.team)
                ]
            else:
                gtimes = [
                    gtime
                    for gtime in self.gamematch.gamematchgtime_set.filter(
                        start_minute__lt = self.minute,
                        stop_minute__gte = self.minute,
                    )
                ]
            if gtimes:
                self.goal_keeper = gtimes[0].player


    def async_save_action(self, *args, **kwargs):
        #if(self.team):
        #    self.team.async_resave()

        if(self.goal_player):
            self.goal_player.resave_player2team_set()

        if(self.goal_keeper):
            self.goal_keeper.resave_player2team_set()
        if self.assistant_1 != None:
            self.assistant_1.resave_player2team_set()
            if self.assistant_2 != None:
                self.assistant_2.resave_player2team_set()
        #else:
        #    [p.resave_player2team_set() for p in self.trans_players.all()]





    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: гол"
        verbose_name_plural = "Игры: матчи: голы"
