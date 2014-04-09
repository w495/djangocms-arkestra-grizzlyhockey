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
        verbose_name=u"Игры",
        blank=True,
        null=True,
    )

    nwins = models.IntegerField(
        verbose_name=u"Выиграли",
        blank=True,
        null=True,
    )

    nloses = models.IntegerField(
        verbose_name=u"Проиграли",
        blank=True,
        null=True,
    )

    ndraws = models.IntegerField(
        verbose_name=u"Ничьи",
        blank=True,
        null=True,
    )

    npoints = models.IntegerField(
        verbose_name=u"Очки",
        blank=True,
        null=True,
    )


    # alter table grizzly_team add ngoals int(11) default null;
    ngoals = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
    )


    # alter table grizzly_team add nmisses int(11) default null;
    nmisses = models.IntegerField(
        verbose_name=u"Пропуски",
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


    def get_ndraws(self):
        da = self.gamematch_a.filter(score_a = models.F('score_b')).count()
        db = self.gamematch_b.filter(score_b = models.F('score_a')).count()
        return da + db


    def get_ngames(self):
        n = self.nwins + self.nloses + self.ndraws
        return n


    def get_ngoals(self):
        wa =  self.gamematch_a.aggregate(models.Sum('score_a')).get('score_a__sum', 0)
        wb =  self.gamematch_b.aggregate(models.Sum('score_b')).get('score_b__sum', 0)
        if(not wa):
            wa = 0
        if(not wb):
            wb = 0
        n = (wa + wb);
        return n

    def get_nmisses(self):
        la =  self.gamematch_a.aggregate(models.Sum('score_b')).get('score_b__sum', 0)
        lb =  self.gamematch_b.aggregate(models.Sum('score_a')).get('score_a__sum', 0)
        if(not la):
            la = 0
        if(not lb):
            lb = 0
        n = (la + lb);
        return n

    def get_npoints(self):
        res = self.nwins * 2 + self.ndraws
        return res

    def _reindex(self):
        self.nwins  = self.get_nwins()
        self.nloses = self.get_nloses()
        self.ndraws = self.get_ndraws()
        self.ngames = self.get_ngames()
        self.npoints = self.get_npoints()
        self.nmisses = self.get_nmisses()
        self.ngoals = self.get_ngoals()
        [p2t.reindex() for p2t in self.player2team_set.all()]


    def reindex(self):
        #>>> from grizzly.models import Team
        #>>> [x.reindex() for x in Team.objects.all()]
        
        self._reindex()
        self.save()


    def save(self, *args, **kwargs):
        self._reindex()
        return super(Team, self).save(*args, **kwargs)


    class Meta:
        ordering = [
            '-npoints',
            '-nwins',
            '-ndraws',
            '-ngames',
        ]
        app_label = "grizzly"
        verbose_name = "команду"
        verbose_name_plural = "команды"
