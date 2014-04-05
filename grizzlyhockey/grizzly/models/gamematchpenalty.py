# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj


class GameMatchPenalty (AbsObj):


    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )



    # alter table grizzly_gamematchpenalty add team_id int(11) default null;
    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда",
    )

    # alter table grizzly_gamematchpenalty add player_id int(11) default null;
    player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игрок",
        related_name="player"
    )

    # alter table grizzly_gamematchpenalty add gl_player_id int(11) default null;
    gl_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"вратарь",
        related_name="gl_player"
    )


    a = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"А"
    )


    b = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"Б"
    )

    gla = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"Вр А"
    )

    glb = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"Вр Б"
    )


    result  = models.NullBooleanField(
        blank = True,
        null = True,
        verbose_name = u"Результат"
    )

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: матч: штрафные броски после игры"
        verbose_name_plural = "Игры: матчи: штрафные броски после игры"
