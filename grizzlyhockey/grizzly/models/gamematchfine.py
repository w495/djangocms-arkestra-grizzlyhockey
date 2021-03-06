# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj
#from player2team import Player2Team
from gameseason import Player2Team

class GameMatchFine (AbsObj):

    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )

    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда",
        related_name="team",
    )

    ##
    ## Фактическое начало отбывания наказания
    ##
    start_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время начала"
    )

    ##
    ## Фактическое окончание штрафного времени
    ##
    stop_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время конца"
    )
    ##
    ## Количество штрафа (в минутах)
    ## ALTER TABLE grizzly_gamematchfine ADD minutes integer default 0;
    ##
    minutes = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"время штрафа (в минутах)",
        default=0
    )
    
    ##
    ## Игрок,
    ##
    fine_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игрок"
    )

    ##
    ## Тип нарушения
    ##
    type = models.ForeignKey(
        'GameFineType',
        blank=True,
        null=True,
        verbose_name=u"тип"
    )

    def async_save_action(self, *args, **kwargs):
        self.fine_player.resave_player2team_set()


    def pre_save_action(self):
        if self.minutes == 20 or self.minutes >= 25:
            fine_players = Player2Team.objects.filter(team__id=self.team.id, player__id=self.fine_player.id)
            if len(fine_players) > 0:
                for player in fine_players:
                    player.is_disqualified = True
                    player.save()
        


    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игра: матч: штраф"
        verbose_name_plural = "Игры: матчи: штрафы"


