# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj
from team import Team
from gameseason import GameSeason

from gametournamentregular import GameTournamentRegular
from gametournamentplayoff import GameTournamentPlayOff
#from player2team import Player2Team
from gameseason import Player2Team
from gameseason import GameSeason
from gameseason import Team2Stat
from gameseason import TeamStatEntry
from gameseason import TeamStat
from gameseason import PlayerStat
from gameseason import Player2Stat
from absobj import AbsObj
from django.db.models import Q

class Division2Stat(AbsObj):
    
    team2stat = models.ManyToManyField(
        'Team2Stat',
        blank = True,
        null = True,
        verbose_name = u"Team2Stat"
    )
    
    season = models.ForeignKey(
        'GameSeason',
        blank = True,
        null = True,
        verbose_name = u"сезон"
    )
    
    def post_save_action(self):
        for team2stat in self.team2stat.all():

            regular_score = team2stat.teamstat.teamstat_regular
            playoff_score = team2stat.teamstat.teamstat_playoff
            sum_score = team2stat.teamstat.teamstat_all
            
            team = team2stat.team
            nwins = 0
            nloses = 0
            ndraws = 0
            ngoals = 0
            nmisses = 0
            for regular in self.season.regulars.all():
               games = list()
               games += [ game.id for game in regular.gamematch_set.filter(Q(team_a = team)).distinct() ]
               games += [ game.id for game in regular.gamematch_set.filter(Q(team_b = team)).distinct() ]
               
               nwins += team.gamematch_a.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               nwins += team.gamematch_b.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               
               nloses += team.gamematch_a.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               nloses += team.gamematch_b.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               
               ndraws += team.gamematch_a.filter(Q(score_b = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               ndraws += team.gamematch_b.filter(Q(score_a = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               
               wa =  sum( x.score_a for x in team.gamematch_a.filter(id__in = games).distinct().exclude(score_a__isnull=True))
               wb =  sum( x.score_b for x in team.gamematch_b.filter(id__in = games).distinct().exclude(score_b__isnull=True))
               if(not wa):
                   wa = 0
               if(not wb):
                   wb = 0
               ngoals += (wa + wb);
               
               la =  sum( x.score_b for x in team.gamematch_a.filter(id__in = games).exclude(score_b__isnull=True).distinct())
               lb =  sum( x.score_a for x in team.gamematch_b.filter(id__in = games).exclude(score_a__isnull=True).distinct())
               if(not la):
                   la = 0
               if(not lb):
                   lb = 0
               nmisses += (la + lb)
            
            ngames = nwins + nloses + ndraws
            npoints = nwins * 2 + ndraws
            
            regular_score.nwins = nwins
            regular_score.nloses = nloses
            regular_score.ndraws = ndraws
            regular_score.npoints = npoints
            regular_score.ngames = ngames
            regular_score.ngoals = ngoals
            regular_score.nmisses = nmisses
            regular_score.save()
             
            nwins = 0
            nloses = 0
            ndraws = 0
            ngoals = 0
            nmisses = 0
            
            for regular in self.season.playoff.all():
                
               games = list()
               games += [ game.id for game in regular.gamematch_set.filter(Q(team_a = team)).distinct() ]
               games += [ game.id for game in regular.gamematch_set.filter(Q(team_b = team)).distinct() ]
               
               nwins += team.gamematch_a.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               nwins += team.gamematch_b.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               
               nloses += team.gamematch_a.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               nloses += team.gamematch_b.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               
               ndraws += team.gamematch_a.filter(Q(score_b = models.F('score_a')) & Q(id__in = games) ).distinct().count()
               ndraws += team.gamematch_b.filter(Q(score_a = models.F('score_b')) & Q(id__in = games) ).distinct().count()
               
               wa =  sum( x.score_a for x in team.gamematch_a.filter(id__in = games).distinct().exclude(score_a__isnull=True))
               wb =  sum( x.score_b for x in team.gamematch_b.filter(id__in = games).distinct().exclude(score_b__isnull=True))
               if(not wa):
                   wa = 0
               if(not wb):
                   wb = 0
               ngoals += (wa + wb)
               
               la =  sum( x.score_b for x in team.gamematch_a.filter(id__in = games).exclude(score_b__isnull=True).distinct())
               lb =  sum( x.score_a for x in team.gamematch_b.filter(id__in = games).exclude(score_a__isnull=True).distinct())
               if(not la):
                   la = 0
               if(not lb):
                   lb = 0
               nmisses += (la + lb)
            
            ngames = nwins + nloses + ndraws
            npoints = nwins * 2 + ndraws
            
            playoff_score.nwins = nwins
            playoff_score.nloses = nloses
            playoff_score.ndraws = ndraws
            playoff_score.npoints = npoints
            playoff_score.ngames = ngames
            playoff_score.ngoals = ngoals
            playoff_score.nmisses = nmisses
            playoff_score.save()
            
            sum_score.nwins = regular_score.nwins + playoff_score.nwins
            sum_score.nloses = regular_score.nloses + playoff_score.nloses
            sum_score.ndraws = regular_score.ndraws + playoff_score.ndraws
            sum_score.npoints = regular_score.npoints + playoff_score.npoints
            sum_score.ngames = regular_score.ngames + playoff_score.ngames
            sum_score.ngoals = regular_score.ngoals + playoff_score.ngoals
            sum_score.nmisses = regular_score.nmisses + playoff_score.nmisses
            sum_score.save()
            

class GameDivision(AbsGameObj):

    gameseasons = models.ManyToManyField(
        'GameSeason',
        blank=True,
        null=True,
        through=GameSeason.gamedivisions.through,
        verbose_name=u"сезоны"
    )

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        through=Team.gamedivisions.through,
        verbose_name=u"команды"
    )

    gametournamentregulars = models.ManyToManyField(
        'GameTournamentRegular',
        blank=True,
        null=True,
        through=GameTournamentRegular.gamedivisions.through,
        verbose_name=u"регулярные чемпионаты"
    )

    gametournamentplayoffs = models.ManyToManyField(
        'GameTournamentPlayOff',
        blank=True,
        null=True,
        through=GameTournamentPlayOff.gamedivisions.through,
        verbose_name=u"play-off"
    )
    
    teams_stats = models.ManyToManyField(
        'Division2Stat',
        blank=True,
        null=True,
        verbose_name=u"play-off"
    )
    
    def create_season(self, season, tour):
        if (tour in self.gametournamentregulars.all() or tour in self.gametournamentplayoffs.all()) and len(self.teams_stats.filter(season=season)) > 0:
            print "Skip it"
            print season.id
            print tour in self.gametournamentregulars.all()
            print tour in self.gametournamentplayoffs.all()
            return
        division2stat = Division2Stat(season=season)
        for team in self.teams.all():
            #print dir(team.stats)
            #return
            
            team_stats = TeamStat.objects.filter(season=season)
            #if len(team_stats) > 0 and len(Team2Stat.objects.filter(team=team, teamstat__in=team_stats)) > 0:
            #    continue
            
            all_stat = TeamStatEntry()
            regular_stat = TeamStatEntry()
            playoff_stat = TeamStatEntry()
            
            all_stat.save()
            regular_stat.save()
            playoff_stat.save()
            
            team_stat = TeamStat(season=season,
                                 teamstat_all=all_stat,
                                 teamstat_regular=regular_stat,
                                 teamstat_playoff=playoff_stat)
            
            team_stat.save()
            team2stat = Team2Stat(team=team, teamstat=team_stat)
            team2stat.save()
            division2stat.save()
            division2stat.team2stat.add(team2stat)            
        division2stat.save()
        self.teams_stats.add(division2stat)
        self.save()
            
    
    def get_some_p2t(self, *args):
        teams = [team for team  in self.teams.all()]
        objs = [x for x in Player2Team.objects.filter(team__in = teams).order_by(*args)]
        return objs
    
    def get_some_p2t_new(self, *args):
        last_season = self.teams_stats.all().order_by("-season__start_datetime")
        if len(last_season) == 0:
            return None
        division2stat = last_season[0]
        last_season = last_season[0].season
        players = list()
        for x in Player2Team.objects.filter(team__in = self.teams.all(), stats__season=last_season).order_by(*args):
            stats = x.stats.filter(season=last_season)
            if len(stats) > 0:
                players.append(stats[0])
        return players
    
    def get_some_p2t_goalkeeper(self, *args):
        teams = [team for team  in self.teams.all()]
        objs = [x for x in Player2Team.objects.filter(team__in = teams, player__role = "Вратарь").exclude(safety_factor = None).order_by(*args)]
        return objs
    
    def get_some_p2t_goalkeeper_new(self, *args):
        last_season = self.teams_stats.all().order_by("-season__start_datetime")
        if len(last_season) == 0:
            return None
        division2stat = last_season[0]
        last_season = last_season[0].season
        teams = division2stat.team2stat.all()
        objs = [x for x in Player2Stat.objects.filter(playerstat__season_id = last_season.id, player2team__player__role = "Вратарь" ).exclude(playerstat__safety_factor = None).order_by(*args)]
        return objs 
 
    def get_p2t(self):
        objs = self.get_some_p2t('-ngoalsntrans')
        return objs
    
    def get_p2t_new(self):
        objs = self.get_some_p2t_new('-stats__ngoalsntrans')
        return objs
    
    def get_max_some_p2t(self, *args):
        objs = self.get_some_p2t(*args)
        if(objs):
            return objs[0:4]
            return objs[0]
        return None
    
    def get_max_some_p2t_new(self, *args):
        objs = self.get_some_p2t_new(*args)
        if(objs):
            return objs[0:4]
            return objs[0]
        return None
    
    def get_max_some_p2t_goalkeeper(self, *args):
        objs = self.get_some_p2t_goalkeeper(*args)
        if(objs):
            return objs[0:4]
            return objs[0]
        return None
    
    def get_max_some_p2t_goalkeeper_new(self, *args):
        objs = self.get_some_p2t_goalkeeper_new(*args)
        if(objs):
            return objs[0:4]
            return objs[0]
        return None
    
    def get_max_ngoalsntrans_p2t(self):
        return self.get_max_some_p2t('-ngoalsntrans')
    
    def get_max_ngoalsntrans_p2t_new(self):
        return self.get_max_some_p2t_new('-stats__ngoalsntrans')

    def get_max_ngoals_p2t(self):
        return self.get_max_some_p2t('-ngoals')
    
    def get_max_ngoals_p2t_new(self):
        return self.get_max_some_p2t_new('-stats__ngoals')

    def get_max_ntrans_p2t(self):
        return self.get_max_some_p2t('-ntrans')
    
    def get_max_ntrans_p2t_new(self):
        return self.get_max_some_p2t_new('-stats__ntrans','-stats__ngoalsntrans')
    
    def get_min_nmisses_p2t(self):
        return self.get_max_some_p2t_goalkeeper('safety_factor', '-ngames')

    def get_min_nmisses_p2t_new(self):
        return self.get_max_some_p2t_goalkeeper_new('playerstat__safety_factor', '-playerstat__ngames')

    def get_min_safety_factor_p2t(self):
        objs = self.get_some_p2t('safety_factor')
        res = [o for o in objs if o.safety_factor != None]
        if(res):
            return res[0]
        return None
    
    def get_min_safety_factor_p2t_new(self):
        objs = self.get_some_p2t_new('playerstat__safety_factor')
        res = [o for o in objs if o.safety_factor != None]
        if(res):
            return res[0]
        return None

    def post_save_action(self):
        [team.async_resave() for team in self.team_set.all()]
        [stat.save() for stat in self.teams_stats.all()]

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: дивизион"
        verbose_name_plural = "Игры: дивизионы"
