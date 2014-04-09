# -*- coding: utf-8 -*-

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

    # alter table grizzly_player2team add ntrans int(11) default null;
    ntrans = models.IntegerField(
        verbose_name=u"Передачи",
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
            x = self.player.gamematchgoal_goal.filter(team = self.team).count()
            return x
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


    def reindex(self):
        self.ngoals = self.get_ngoals()
        self.ntrans = self.get_ntrans()
        self.nfines = self.get_nfines()
        self.ngames = self.get_ngames()
        self.save()


    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока: команду"
        verbose_name_plural = "игроки: команды"
