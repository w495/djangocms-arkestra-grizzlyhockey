# -*- coding: utf-8 -*-

from django.db import models

from absobj import AbsObj
from django_cached_functions import cached_function
from django.db.models import Q
from gameseason import GameSeason


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

    def get_last_season(self):
        seasons = GameSeason.objects.filter().order_by('-start_datetime')
        if len(seasons) > 0:
            return seasons[0]
        return None
    
    def get_division_query(self):
        season = self.get_last_season()
        if season == None:
            return None
        divisions = self.gamedivisions.filter(gameseasons = season)
        q = Q()
        for division in divisions:
            q |= Q(gametournamentregular__gamedivisions=division)
        return q

    def get_nwins(self):
        wa = self.gamematch_a.filter(Q(score_a__gt = models.F('score_b')) & self.query_set).distinct().count()
        wb = self.gamematch_b.filter(Q(score_b__gt = models.F('score_a')) & self.query_set).distinct().count()
        
        return wa + wb

    def get_nloses(self):
        la = self.gamematch_a.filter(Q(score_a__lt = models.F('score_b')) & self.query_set).distinct().count()
        lb = self.gamematch_b.filter(Q(score_b__lt = models.F('score_a')) & self.query_set).distinct().count()
        
        return la + lb


    def get_ndraws(self):
        da = self.gamematch_a.filter(Q(score_a = models.F('score_b')) & self.query_set).distinct().count()
        db = self.gamematch_b.filter(Q(score_b = models.F('score_a')) & self.query_set).distinct().count()
        return da + db


    def get_ngames(self):
        n = self.nwins + self.nloses + self.ndraws
        return n


    def get_ngoals(self):
        wa =  sum( x.score_a for x in self.gamematch_a.filter(self.query_set).distinct().exclude(score_a__isnull=True))
        wb =  sum( x.score_b for x in self.gamematch_b.filter(self.query_set).distinct().exclude(score_b__isnull=True))
        if(not wa):
            wa = 0
        if(not wb):
            wb = 0
        n = (wa + wb);
        return n

    def get_nmisses(self):
        la =  sum( x.score_b for x in self.gamematch_a.filter(self.query_set).exclude(score_b__isnull=True).distinct())
        lb =  sum( x.score_a for x in self.gamematch_b.filter(self.query_set).exclude(score_a__isnull=True).distinct())
        if(not la):
            la = 0
        if(not lb):
            lb = 0
        n = (la + lb);
        return n

    def get_npoints(self):
        res = self.nwins * 2 + self.ndraws
        return res

    def pre_save_action(self):
        #self.query_set = self.get_division_query()
        #self.nwins  = self.get_nwins()
        #self.nloses = self.get_nloses()
        #self.ndraws = self.get_ndraws()
        #self.ngames = self.get_ngames()
        #self.npoints = self.get_npoints()
        #self.nmisses = self.get_nmisses()
        #self.ngoals = self.get_ngoals()
        [ division.resave() for division in self.gamedivisions.all() ]
        [ p2t.resave() for p2t in self.player2team_set.all() ]

    def async_save_action(self):
        [ division.resave() for division in self.gamedivisions.all() ]
        [p2t.async_resave() for p2t in self.player2team_set.all()]


    class Meta:
        ordering = [
            '-npoints',
            '-nwins',
            '-ndraws',
            '-ngames',
            '-ngoals',
            'nmisses',
        ]
        app_label = "grizzly"
        verbose_name = "команду"
        verbose_name_plural = "команды"
