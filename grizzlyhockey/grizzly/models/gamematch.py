# -*- coding: utf-8 -*-
import gevent
import gevent.socket
import uuid

from django.db import models
from absgameobj import AbsGameObj


import time

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


    gametournamentregular = models.ForeignKey(
        'GameTournamentRegular',
        blank=True,
        null=True,
        verbose_name=u"Турнир"
    )


    def save(self, *args, **kwargs):
        res = super(GameMatch, self).save(*args, **kwargs)


        gevent.spawn(lambda: self.reindex(word=uuid.uuid4()))

        return res


    def reindex(self, word, *args, **kwargs):

        f = open('x', 'w')
        f.write("x-%s"%word)

        self.team_a.reindex()
        self.team_b.reindex()


    #def __str__(self):
        #rink = ""
        #if(self.rink):
            #rink = "(%s)"%self.rink
        #team_a = ""
        #if(self.team_a):
            #team_a = "«%s»"%self.team_a.name

        #team_b = ""
        #if(self.team_b):
            #team_b = "«%s»"%self.team_b.name

        #return u"%s (%s): «%s» × «%s»"%(self.name, rink, team_a, team_b)

    #def __unicode__(self):
        #rink = ""
        #if(self.rink):
            #rink = "(%s)"%self.rink
        #team_a = ""
        #if(self.team_a):
            #team_a = "«%s»"%self.team_a.name

        #team_b = ""
        #if(self.team_b):
            #team_b = "«%s»"%self.team_b.name

        #return u"%s (%s): «%s» × «%s»"%(self.name, rink, team_a, team_b)


    class Meta:
        ordering = ['ctime',]
        app_label = "grizzly"
        verbose_name = "Игры: матч"
        verbose_name_plural = "Игры: матчи"
