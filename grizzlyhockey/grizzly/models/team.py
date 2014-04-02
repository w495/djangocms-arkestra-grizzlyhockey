# -*- coding: utf-8 -*-

from django.db import models

from absobj import AbsObj


class Team(AbsObj):

    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"дата создания"
    )

    ##
    ## хак, для создания двусторонней многие-ко-многим.
    ## http://stackoverflow.com/questions/660260/django-admin-form-for-many-to-many-relationship
    ##

    players = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        through='Player2Team',
        verbose_name=u"игроки"
    )

    teamschedules = models.ManyToManyField(
        'TeamSchedule',
        blank=True,
        null=True,
        verbose_name=u"расписания"
    )

    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    def get_ngames(self):
        n = self.gamematch_a.count() + self.gamematch_b.count()
        return n

    def get_nwins(self):
        wa = self.gamematch_a.filter(score_a__gt = models.F('score_b')).count()
        wb = self.gamematch_a.filter(score_b__gt = models.F('score_a')).count()
        return wa + wb


    def get_nloses(self):
        la = self.gamematch_a.filter(score_a__lt = models.F('score_b')).count()
        lb = self.gamematch_a.filter(score_b__lt = models.F('score_a')).count()
        return la + lb


    def get_npoints(self):
        n = 100 * self.get_nwins() / self.get_ngames() / 100.0

        return n



    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "команду"
        verbose_name_plural = "команды"
