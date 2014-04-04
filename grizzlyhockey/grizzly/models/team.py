# -*- coding: utf-8 -*-

from django.db import models

from absobj import AbsObj
from django_cached_functions import cached_function

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

    ngames = models.IntegerField(
        verbose_name=u"Количество игр (Ч)",
        blank=True,
        null=True,
    )

    nwins = models.IntegerField(
        verbose_name=u"Количество побед (Ч)",
        blank=True,
        null=True,
    )

    nloses = models.IntegerField(
        verbose_name=u"Количество поражений (Ч)",
        blank=True,
        null=True,
    )

    npoints = models.IntegerField(
        verbose_name=u"Количество очков (Ч)",
        blank=True,
        null=True,
    )

    def get_nwins(self):
        wa = self.gamematch_a.filter(score_a__gt = models.F('score_b')).count()
        wb = self.gamematch_b.filter(score_b__gt = models.F('score_a')).count()
        return wa + wb

    def get_nloses(self):
        la = self.gamematch_a.filter(score_a__lt = models.F('score_b')).count()
        lb = self.gamematch_b.filter(score_b__lt = models.F('score_a')).count()
        return la + lb

    def get_ngames(self):
        n = self.get_nwins() + self.get_nwins()
        return n

    def get_npoints(self):
        wa =  self.gamematch_a.aggregate(models.Sum('score_a')).get('score_a__sum', 0)
        wb =  self.gamematch_b.aggregate(models.Sum('score_b')).get('score_b__sum', 0)
        if(not wa):
            wa = 0
        if(not wb):
            wb = 0
        la =  self.gamematch_a.aggregate(models.Sum('score_b')).get('score_b__sum', 0)
        lb =  self.gamematch_b.aggregate(models.Sum('score_a')).get('score_a__sum', 0)
        if(not la):
            la = 0
        if(not lb):
            lb = 0
        n = (wa + wb);
        return n

    def _reindex(self):
        self.ngames = self.get_ngames()
        self.nwins  = self.get_nwins()
        self.nloses = self.get_nloses()
        self.npoints = self.get_npoints()

    def reindex(self):
        #>>> from grizzly.models import Team
        #>>> [x.reindex() for x in Team.objects.all()]
        
        self._reindex()
        self.save()

    def save(self, *args, **kwargs):
        self._reindex()
        return super(Team, self).save(*args, **kwargs)


    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "команду"
        verbose_name_plural = "команды"
