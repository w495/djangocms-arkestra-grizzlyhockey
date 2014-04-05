# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers
from gamematchgoal import GameMatchGoal

class Player(AbsPers):

    insurance_type = models.ForeignKey(
        'InsuranceType',
        blank = True,
        null = True,
        verbose_name = u"тип страховки"
    )

    height = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"рост"
    )

    weight = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"вес"
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

    qualification = models.TextField(
        blank = True,
        null = True,
        verbose_name = u"квалификация"
    )

    status = models.ForeignKey(
        'PlayerStatus',
        blank = True,
        null = True,
        verbose_name = u"статус"
    )

    type = models.ForeignKey(
        'PlayerType',
        blank = True,
        null = True,
        verbose_name = u"тип"
    )

    teams = models.ManyToManyField(
        'Team',
        blank = True,
        null = True,
        through='Player2Team',
        verbose_name = u"команды"
    )

    gamematchgoal_trans = models.ManyToManyField(
        'GameMatchGoal',
        blank=True,
        null=True,
        through=GameMatchGoal.trans_players.through,
        verbose_name=u"игроки, сделавшие результативную передачу"
    )


    def reindex(self):
        [p2t.reindex() for p2t in self.player2team_set.all()]

    def __str__(self):
        return u"%s, %s %s %s"%(self.game_number, self.second_name, self.first_name, self.patronymic)

    def __unicode__(self):
        return u"%s, %s %s %s"%(self.game_number, self.second_name, self.first_name, self.patronymic)


    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока"
        verbose_name_plural = "игроки"
