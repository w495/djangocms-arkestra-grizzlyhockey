# -*- coding: utf-8 -*-
import logging

from django.db import models
from abspers import AbsPers
from absobj import AbsObj

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


    def get_ngames(self):
        if (self.player):
            ga = self.player.gamematch_a.filter(team_a = self.team).count()
            gb = self.player.gamematch_b.filter(team_b = self.team).count()
            return ga + gb
        return 0

    def get_ngoals(self):
        if (self.player):
            x = self.player.gamematchgoal_goal.filter().count()
            return x
        return 0

    def get_nmisses(self):
        if (self.player):
            x = self.player.gamematchgoal_miss.filter().count()
            return x
        return 0


    def get_goalminutes(self):
        if (self.player):
            minutes = sum([
                gtime.get_diff_minute()
                for gtime in self.player.gamematchgtime_set.all()
            ])
            return minutes
        return 0

    def get_nfines(self):
        if (self.player):
            x = self.player.gamematchfine_set.filter(team = self.team).count()
            return x
        return 0

    def get_ntrans(self):
        if (self.player):
            x = self.player.gamematchgoal_trans.filter(team = self.team).count()
            return x
        return 0

    def get_safety_factor(self):
        if(not self.goalminutes):
            return None

        mins = self.team.ngames * 60
        if(1.0 * self.goalminutes / mins < 1.0 / 3)
            return None

        return (self.nmisses * 6000 / self.goalminutes)


    def pre_save_action(self):
        self.ngoals = self.get_ngoals()
        self.nmisses =  self.get_nmisses()

        self.ntrans = self.get_ntrans()
        self.nfines = self.get_nfines()
        self.ngames = self.get_ngames()
        self.goalminutes = self.get_goalminutes()

        self.safety_factor =  self.get_safety_factor()

        self.ngoalsntrans = self.ngoals + self.ntrans



    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока: команду"
        verbose_name_plural = "игроки: команды"
