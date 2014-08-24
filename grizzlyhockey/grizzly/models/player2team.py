# -*- coding: utf-8 -*-
import logging

from django.db import models
from abspers import AbsPers
from absobj import AbsObj
from gamematchgoal import GameMatchGoal
from gamematchgtime import GameMatchGTime
from gamematch import GameMatch
from gameseason import GameSeason
from django.db.models import Q
import time

class Player2Team(AbsObj):

    status = models.ForeignKey(
        'PlayerStatus',
        blank = True,
        null = True,
        verbose_name = u"статус"
    )

    game_number = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"игровой номер"
    )

    role = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"амплуа"
    )

    team = models.ForeignKey(
        'Team',
        blank = True,
        null = True,
        verbose_name = u"команда"
    )

    player = models.ForeignKey(
        'Player',
        blank = True,
        null = True,
        verbose_name = u"игрок"
    )


    #alter table grizzly_player2team add ngames int(11) default null;
    ngames = models.IntegerField(
        verbose_name=u"Игры",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add nfines int(11) default null;
    nfines = models.IntegerField(
        verbose_name=u"Штрафы",
        blank=True,
        null=True,
        default=0
    )
    
    # alter table grizzly_player2team add nfines_minutes int(11) default null;
    nfines_minutes = models.IntegerField(
        verbose_name=u"Штрафы (в минутах)",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ngoals int(11) default null;
    ngoals = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add nmisses int(11) default null;
    nmisses = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add goalminutes int(11) default null;
    goalminutes = models.IntegerField(
        verbose_name=u"",
        blank=True,
        null=True,
        default=0
    )



    # alter table grizzly_player2team add safety_factor int(11) default null;
    safety_factor = models.IntegerField(
        verbose_name=u"safety_factor",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ntrans int(11) default null;
    ntrans = models.IntegerField(
        verbose_name=u"Передачи",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add ngoalsntrans int(11) default null;
    ngoalsntrans = models.IntegerField(
        verbose_name=u"Голы и Передачи",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add npoints int(11) default null;
    npoints = models.IntegerField(
        verbose_name=u"Очки",
        blank=True,
        null=True,
        default=0
    )

    #  alter table grizzly_player add is_disqualified bool NOT NULL;
    is_disqualified = models.BooleanField(
        default=False,
        verbose_name = u'дисквалифицирован'
    )

    def get_last_season(self):
        seasons = GameSeason.objects.filter().order_by('-start_datetime')
        if len(seasons) > 0:
            return seasons[0]
        return None
    
    def get_division_query(self):
        season = self.get_last_season()
        if season == None:
            return None
        divisions = season.gamedivisions.all()
        q = Q()
        for division in divisions:
            q |= Q(gametournamentregular__gamedivisions=division)
            q |= Q(gametournamentplayoff__gamedivisions=division)
        return q

    def get_ngames(self):
        if (self.player):
            ga = self.player.gamematch_a.filter(Q(team_a = self.team) & self.query_set).distinct().count()
            gb = self.player.gamematch_b.filter(Q(team_b = self.team) & self.query_set).distinct().count()
            return ga + gb
        return 0

    def get_ngoals(self):
        if (self.player):
            x = GameMatchGoal.objects.filter(goal_player=self.player, gamematch__in = self.season_games).distinct().count()
            return x
        return 0

    def get_nmisses(self):
        if (self.player):
            x = self.player.gamematchgoal_miss.filter(gamematch__in = self.season_games).count()
            return x
        return 0


    def get_goalminutes(self):
        if (self.player):
            minutes = sum([
                gtime.get_diff_minute()
                for gtime in self.player.gamematchgtime_set.filter(player=self.player, gamematch__in = self.season_games).distinct()
            ])
            
            return minutes / 2
        return 0

    def get_nfines(self):
        if (self.player):
            x = self.player.gamematchfine_set.filter(team = self.team, gamematch__in = self.season_games).count()
            return x
        return 0
    
    def get_nfines_minutes(self):
        if (self.player):
            fines = sum(fine.minutes for fine in self.player.gamematchfine_set.filter(team = self.team, gamematch__in = self.season_games))
            return fines
        return 0
    
    def get_ntrans(self):
        if (self.player):
            assistant_count = len(GameMatchGoal.objects.filter(Q(assistant_1 = self.player) | Q(assistant_2 = self.player), gamematch__in = self.season_games))
            # there isn't two same assistant
            x = assistant_count
            x += self.player.gamematchgoal_trans.filter(team = self.team, gamematch__in = self.season_games).count()
            return x
        return 0

    def get_safety_factor(self):
        if(not self.goalminutes or self.team.ngames == 0):
            return None

        mins = self.team.ngames * 60
        if(1.0 * self.goalminutes / mins < 1.0 / 3):
            return None

        return (self.nmisses * 6000 / self.goalminutes)


    def pre_save_action(self):
        self.query_set = self.get_division_query()
        self.season_games = GameMatch.objects.filter(self.query_set).distinct()
        self.ngoals = self.get_ngoals()
        self.nmisses =  self.get_nmisses()

        self.ntrans = self.get_ntrans()
        self.nfines = self.get_nfines()
        self.nfines_minutes = self.get_nfines_minutes()
        self.ngames = self.get_ngames()
        self.goalminutes = self.get_goalminutes()

        self.safety_factor =  self.get_safety_factor()

        self.ngoalsntrans = self.ngoals + self.ntrans



    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока: команду"
        verbose_name_plural = "игроки: команды"
