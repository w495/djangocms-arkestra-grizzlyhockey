# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameMatchGoal (AbsObj):

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
    )

    time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время"
    )

    goalno = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"номер шайбы"
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

    def save(self, *args, **kwargs):
        goal_player.reindex()
        [p.reindex() for p in self.trans_players.all()]
        return super(GameMatchGoal, self).save(*args, **kwargs)


    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: гол"
        verbose_name_plural = "Игры: матчи: голы"
