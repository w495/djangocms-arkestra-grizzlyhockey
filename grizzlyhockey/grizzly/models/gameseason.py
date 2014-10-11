# -*- coding: utf-8 -*-

from django.db import models
from absgameobj import AbsGameObj


import logging
from abspers import AbsPers
from absobj import AbsObj
from gamematchgoal import GameMatchGoal
from gamematchgtime import GameMatchGTime
from gamematch import GameMatch
from django.db.models import Q
import time

from django_cached_functions import cached_function


class GameSeason (AbsGameObj):

    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )
    
    regulars = models.ManyToManyField(
        'GameTournamentRegular',
        blank=True,
        null=True,
        verbose_name=u"регулярный чемпионат"
    )
    
    playoff = models.ManyToManyField(
        'GameTournamentPlayOff',
        blank=True,
        null=True,
        verbose_name=u"play-off"
    )
    
    
    def post_save_action(self):
        for tour in self.regulars.all():
            for division in tour.gamedivisions.all():
                #print "AHAHAHAHAHHAHAHAHAHAHAH START CREATE DIVISION"
                division.create_season(self, tour)
            for team in tour.teams.all():
                team.resave()
                if len(Team2Stat.objects.filter(team=team, teamstat__season=self)) == 0:
                    teamstat = TeamStat(season=self)
                    teamstat.save()
                    
                    team2stat = Team2Stat(team=team, teamstat=teamstat)
                    team2stat.save()
                
                for player in team.player2team_set.all():
                    if len(Player2Stat.objects.filter(player2team=player, playerstat__season=self)) != 0:
                        continue
                    stat = PlayerStat(season=self)
                    stat.save()
                    player2stat = Player2Stat(player2team=player, playerstat=stat)
                    player2stat.save()
        
        for tour in self.playoff.all():
            for division in tour.gamedivisions.all():
                division.create_season(self, tour)
            for team in tour.teams.all():
                team.resave()
                if len(Team2Stat.objects.filter(team=team, teamstat__season=self)) == 0:
                    teamstat = TeamStat(season=self)
                    teamstat.save()
                    
                    team2stat = Team2Stat(team=team, teamstat=teamstat)
                    team2stat.save()
                
                for player in team.player2team_set.all():
                    if len(Player2Stat.objects.filter(player2team=player, playerstat__season=self)) != 0:
                        continue
                    stat = PlayerStat(season=self)
                    stat.save()
                    player2stat = Player2Stat(player2team=player, playerstat=stat)
                    player2stat.save()

    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игры: сезон"
        verbose_name_plural = "Игры: сезоны"


# =====================================================================================


class Team2Stat(AbsObj):
    team = models.ForeignKey(
        'Team',
        blank = True,
        null = True,
        verbose_name = u"Team"
    )
    
    teamstat = models.ForeignKey(
        'TeamStat',
        blank = True,
        null = True,
        verbose_name = u"TeamStat"
    )
    
    class Meta:
        app_label = "grizzly"
        verbose_name = "команда: статистика"
        verbose_name_plural = "команды: статистики"

class TeamStat(AbsObj):
    
    season = models.ForeignKey(
        'GameSeason',
        blank = True,
        null = True,
        verbose_name = u"сезон"
    )
    
    teamstat_all = models.ForeignKey(
        'TeamStatEntry',
        blank = True,
        null = True,
        verbose_name = u"TeamStat",
        related_name='teamstat_all'
    )
    
    teamstat_regular = models.ForeignKey(
        'TeamStatEntry',
        blank = True,
        null = True,
        verbose_name = u"TeamStatRegular",
        related_name='regularstat'
    )
    
    teamstat_playoff = models.ForeignKey(
        'TeamStatEntry',
        blank = True,
        null = True,
        verbose_name = u"TeamStatPlayoff",
        related_name='playoffstat'
    )
    

class TeamStatEntry(AbsObj):
    
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
    
    stats = models.ManyToManyField(
        'TeamStat',
        blank = True,
        null = True,
        through='Team2Stat',
        verbose_name = u"статистика",
        related_name='team_stat_set'
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
        try:
            if self.stats is None:
                return
        except:
            return
        for season in [ haha.season for haha in self.stats.all() ]:
            team2stats = Team2Stat.objects.filter(team=self, teamstat__season=season)
            if len(team2stats) != 1:
                # "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SKIP IT"
                continue
            team2stat = Team2Stat.objects.get(team=self, teamstat__season=season)
            
            nwins = 0
            nloses = 0
            ndraws = 0
            ngoals = 0
            nmisses = 0
            for regular in season.regulars.all():
                games = list()
                games += [ game.id for game in regular.gamematch_set.filter(Q(team_a = self)).distinct() ]
                games += [ game.id for game in regular.gamematch_set.filter(Q(team_b = self)).distinct() ]
                
                nwins += self.gamematch_a.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                nwins += self.gamematch_b.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                
                nloses += self.gamematch_a.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                nloses += self.gamematch_b.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                
                ndraws += self.gamematch_a.filter(Q(score_b = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                ndraws += self.gamematch_b.filter(Q(score_a = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                
                wa =  sum( x.score_a for x in self.gamematch_a.filter(id__in = games).distinct().exclude(score_a__isnull=True))
                wb =  sum( x.score_b for x in self.gamematch_b.filter(id__in = games).distinct().exclude(score_b__isnull=True))
                if(not wa):
                    wa = 0
                if(not wb):
                    wb = 0
                ngoals += (wa + wb);
                
                la =  sum( x.score_b for x in self.gamematch_a.filter(id__in = games).exclude(score_b__isnull=True).distinct())
                lb =  sum( x.score_a for x in self.gamematch_b.filter(id__in = games).exclude(score_a__isnull=True).distinct())
                if(not la):
                    la = 0
                if(not lb):
                    lb = 0
                nmisses += (la + lb)
                
            for regular in season.playoff.all():
                
                games = list()
                games += [ game.id for game in regular.gamematch_set.filter(Q(team_a = self)).distinct() ]
                games += [ game.id for game in regular.gamematch_set.filter(Q(team_b = self)).distinct() ]
                
                nwins += self.gamematch_a.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                nwins += self.gamematch_b.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                
                nloses += self.gamematch_a.filter(Q(score_b__gt = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                nloses += self.gamematch_b.filter(Q(score_a__gt = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                
                ndraws += self.gamematch_a.filter(Q(score_b = models.F('score_a')) & Q(id__in = games) ).distinct().count()
                ndraws += self.gamematch_b.filter(Q(score_a = models.F('score_b')) & Q(id__in = games) ).distinct().count()
                
                wa =  sum( x.score_a for x in self.gamematch_a.filter(id__in = games).distinct().exclude(score_a__isnull=True))
                wb =  sum( x.score_b for x in self.gamematch_b.filter(id__in = games).distinct().exclude(score_b__isnull=True))
                if(not wa):
                    wa = 0
                if(not wb):
                    wb = 0
                ngoals += (wa + wb)
                
                la =  sum( x.score_b for x in self.gamematch_a.filter(id__in = games).exclude(score_b__isnull=True).distinct())
                lb =  sum( x.score_a for x in self.gamematch_b.filter(id__in = games).exclude(score_a__isnull=True).distinct())
                if(not la):
                    la = 0
                if(not lb):
                    lb = 0
                nmisses += (la + lb)
        
            
            ngames = nwins + nloses + ndraws
            npoints = nwins * 2 + ndraws
            
            team2stat.teamstat.nwins = nwins
            team2stat.teamstat.nloses = nloses
            team2stat.teamstat.ndraws = ndraws
            team2stat.teamstat.npoints = npoints
            team2stat.teamstat.ngames = ngames
            team2stat.teamstat.ngoals = ngoals
            team2stat.teamstat.nmisses = nmisses
            team2stat.teamstat.save()
        
        self.query_set = self.get_division_query()
        self.nwins  = self.get_nwins()
        self.nloses = self.get_nloses()
        self.ndraws = self.get_ndraws()
        self.ngames = self.get_ngames()
        self.npoints = self.get_npoints()
        self.nmisses = self.get_nmisses()
        self.ngoals = self.get_ngoals()

    def async_save_action(self):
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

# =====================================================================================

class Player2Stat(AbsObj):
    
    player2team = models.ForeignKey(
        'Player2Team',
        blank = True,
        null = True,
        verbose_name = u"Player2Team"
    )
    
    playerstat = models.ForeignKey(
        'PlayerStat',
        blank = True,
        null = True,
        verbose_name = u"PlayerStat"
    )
    
    class Meta:
        app_label = "grizzly"
        verbose_name = "игрок: статистика"
        verbose_name_plural = "игроки: статистики"

class PlayerStat(AbsObj):
    
    season = models.ForeignKey(
        'GameSeason',
        blank = True,
        null = True,
        verbose_name = u"сезон"
    )
    
    #alter table grizzly_player2team add ngames int(11) default null;
    ngames = models.IntegerField(
        verbose_name=u"Игры",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add nfines int(11) default null;
    nfines = models.IntegerField(
        verbose_name=u"Штрафы",
        blank=True,
        null=True,
        default=0
    )
    
    # alter table grizzly_player2team add nfines_minutes int(11) default null;
    nfines_minutes = models.IntegerField(
        verbose_name=u"Штрафы (в минутах)",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ngoals int(11) default null;
    ngoals = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add nmisses int(11) default null;
    nmisses = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add goalminutes int(11) default null;
    goalminutes = models.IntegerField(
        verbose_name=u"",
        blank=True,
        null=True,
        default=0
    )



    # alter table grizzly_player2team add safety_factor int(11) default null;
    safety_factor = models.IntegerField(
        verbose_name=u"safety_factor",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ntrans int(11) default null;
    ntrans = models.IntegerField(
        verbose_name=u"Передачи",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add ngoalsntrans int(11) default null;
    ngoalsntrans = models.IntegerField(
        verbose_name=u"Голы и Передачи",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add npoints int(11) default null;
    npoints = models.IntegerField(
        verbose_name=u"Очки",
        blank=True,
        null=True,
        default=0
    )
    
    class Meta:
        app_label = "grizzly"
        verbose_name = "статистика"
        verbose_name_plural = "статистики"



class Player2Team(AbsObj):

    status = models.ForeignKey(
        'PlayerStatus',
        blank = True,
        null = True,
        verbose_name = u"статус"
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

    team = models.ForeignKey(
        'Team',
        blank = True,
        null = True,
        verbose_name = u"команда"
    )

    player = models.ForeignKey(
        'Player',
        blank = True,
        null = True,
        verbose_name = u"игрок"
    )


    #alter table grizzly_player2team add ngames int(11) default null;
    ngames = models.IntegerField(
        verbose_name=u"Игры",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add nfines int(11) default null;
    nfines = models.IntegerField(
        verbose_name=u"Штрафы",
        blank=True,
        null=True,
        default=0
    )
    
    # alter table grizzly_player2team add nfines_minutes int(11) default null;
    nfines_minutes = models.IntegerField(
        verbose_name=u"Штрафы (в минутах)",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ngoals int(11) default null;
    ngoals = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add nmisses int(11) default null;
    nmisses = models.IntegerField(
        verbose_name=u"Голы",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add goalminutes int(11) default null;
    goalminutes = models.IntegerField(
        verbose_name=u"",
        blank=True,
        null=True,
        default=0
    )



    # alter table grizzly_player2team add safety_factor int(11) default null;
    safety_factor = models.IntegerField(
        verbose_name=u"safety_factor",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add ntrans int(11) default null;
    ntrans = models.IntegerField(
        verbose_name=u"Передачи",
        blank=True,
        null=True,
        default=0
    )


    # alter table grizzly_player2team add ngoalsntrans int(11) default null;
    ngoalsntrans = models.IntegerField(
        verbose_name=u"Голы и Передачи",
        blank=True,
        null=True,
        default=0
    )

    # alter table grizzly_player2team add npoints int(11) default null;
    npoints = models.IntegerField(
        verbose_name=u"Очки",
        blank=True,
        null=True,
        default=0
    )

    #  alter table grizzly_player add is_disqualified bool NOT NULL;
    is_disqualified = models.BooleanField(
        default=False,
        verbose_name = u'дисквалифицирован'
    )
    
    #  alter table grizzly_player add stats int NOT NULL;
    stats = models.ManyToManyField(
        'PlayerStat',
        blank = True,
        null = True,
        through='Player2Stat',
        verbose_name = u"статистика"
    )
    
    def get_last_season(self):
        #seasons = GameSeason.objects.filter().order_by('-start_datetime')
        #if len(seasons) > 0:
        #    return seasons[0]
        return None
    
    def get_division_query(self):
        season = self.get_last_season()
        if season == None:
            return None
        divisions = season.gamedivisions.all()
        q = Q()
        for division in divisions:
            q |= Q(gametournamentregular__gamedivisions=division)
            q |= Q(gametournamentplayoff__gamedivisions=division)
        return q

    def get_ngames(self):
        if (self.player):
            ga = self.player.gamematch_a.filter(Q(team_a = self.team) & self.query_set).distinct().count()
            gb = self.player.gamematch_b.filter(Q(team_b = self.team) & self.query_set).distinct().count()
            return ga + gb
        return 0

    def get_ngoals(self):
        if (self.player):
            x = GameMatchGoal.objects.filter(goal_player=self.player, gamematch__in = self.season_games).distinct().count()
            return x
        return 0

    def get_nmisses(self):
        if (self.player):
            x = self.player.gamematchgoal_miss.filter(gamematch__in = self.season_games).count()
            return x
        return 0


    def get_goalminutes(self):
        if (self.player):
            minutes = sum([
                gtime.get_diff_minute()
                for gtime in self.player.gamematchgtime_set.filter(player=self.player, gamematch__in = self.season_games).distinct()
            ])
            
            return minutes / 2
        return 0

    def get_nfines(self):
        if (self.player):
            x = self.player.gamematchfine_set.filter(team = self.team, gamematch__in = self.season_games).count()
            return x
        return 0
    
    def get_nfines_minutes(self):
        if (self.player):
            fines = sum(fine.minutes for fine in self.player.gamematchfine_set.filter(team = self.team, gamematch__in = self.season_games))
            return fines
        return 0
    
    def get_ntrans(self):
        if (self.player):
            assistant_count = len(GameMatchGoal.objects.filter(Q(assistant_1 = self.player) | Q(assistant_2 = self.player), gamematch__in = self.season_games))
            # there isn't two same assistant
            x = assistant_count
            x += self.player.gamematchgoal_trans.filter(team = self.team, gamematch__in = self.season_games).count()
            return x
        return 0

    def get_safety_factor(self):
        if(not self.goalminutes or self.team.ngames == 0):
            return None

        mins = self.team.ngames * 60
        if(1.0 * self.goalminutes / mins < 1.0 / 3):
            return None

        return (self.nmisses * 6000 / self.goalminutes)
    
    def get_safety_factor(self, playerstat, season):
        #return
        teamstat = Team2Stat.objects.filter(team=self.team, teamstat__season = season)
        if len(teamstat) == 0:
            return None
        teamstat = teamstat[0]
        if(not playerstat.goalminutes or teamstat.teamstat.teamstat_all.ngames == 0):
            return None

        mins = teamstat.teamstat.teamstat_all.ngames * 60
        if(1.0 * playerstat.goalminutes / mins < 1.0 / 3):
            return None

        return (playerstat.nmisses * 6000 / playerstat.goalminutes)


    def pre_save_action(self):
        
        #print "\n\n\n==================== Yabadaa sdad asd\n\n\n"
        #for season in [ haha.season for haha in self.stats.all() ]:
        #    print season.name
        #    player2stats = Player2Stat.objects.filter(player2team=self, playerstat__season=season)
        #    print len(player2stats)
        #    if len(player2stats) != 1:
        #        continue
        #    player2stat = Player2Stat.objects.get(player2team=self, playerstat__season=season)
        #    print "\n\n\n\nOOOOOOOOps\n\n\n\n\n\n"
        #    ngames = 0
        #    nmiss = 0
        #    for regular in season.regulars.all():
        #        ngames += regular.gamematch_set.filter(Q(team_a = self.team) & Q(players_a__id = self.player.id) ).distinct().count()
        #        ngames += regular.gamematch_set.filter(Q(team_b = self.team) & Q(players_b__id = self.player.id) ).distinct().count()
        #        print "\n\n\n\nNgames\n\n\n\n\n\n"
        #        print ngames
        #        games = list()
        #        games += regular.gamematch_set.filter(Q(team_a = self.team)).distinct()
        #        games += regular.gamematch_set.filter(Q(team_b = self.team)).distinct()
        #        nmiss += self.player.gamematchgoal_miss.filter(gamematch__in = games).count()
        #        print "\n\n\n\nNmiss\n\n\n\n\n\n"
        #        print nmiss
        #return
        for season in [ haha.season for haha in self.stats.all() ]:
            player2stats = Player2Stat.objects.filter(player2team=self, playerstat__season=season)
            if len(player2stats) != 1:
                continue
            player2stat = Player2Stat.objects.get(player2team=self, playerstat__season=season)
            ngames = 0
            ngoals = 0
            nmiss = 0
            nfines = 0
            fines = 0
            ntrans = 0
            goalminutes = 0
            #print "\n\n\n\n\n O macarena \n\n\n\n\n\n\n"
            #print player2stat.playerstat.id
            for regular in season.regulars.all():
                ngames += regular.gamematch_set.filter(Q(team_a = self.team) & Q(players_a__id = self.player.id) ).distinct().count()
                ngames += regular.gamematch_set.filter(Q(team_b = self.team) & Q(players_b__id = self.player.id) ).distinct().count()
                
                games = list()
                games += regular.gamematch_set.filter(Q(team_a = self.team)).distinct()
                games += regular.gamematch_set.filter(Q(team_b = self.team)).distinct()
                nmiss += self.player.gamematchgoal_miss.filter(gamematch__in = games).count()
                #print "\n\n\n\nNmiss\n\n\n\n\n\n"
                #print nmiss
                nfines += self.player.gamematchfine_set.filter(team = self.team, gamematch__in = games).count()
                fines += sum(fine.minutes for fine in self.player.gamematchfine_set.filter(team = self.team, gamematch__in = games))
                
                assistant_count = len(GameMatchGoal.objects.filter(Q(assistant_1 = self.player) | Q(assistant_2 = self.player), gamematch__in = games).distinct())
                # there isn't two same assistant
                ntrans += assistant_count
                ntrans += self.player.gamematchgoal_trans.filter(team = self.team, gamematch__in = games).count()
                
                goalminutes += sum([ gtime.get_diff_minute()
                    for gtime in self.player.gamematchgtime_set.filter(player=self.player, gamematch__in = games).distinct()
                ]) / 2
                
                ngoals += GameMatchGoal.objects.filter(goal_player=self.player, gamematch__in = games).distinct().count()
                
            for regular in season.playoff.all():
                ngames += regular.gamematch_set.filter(Q(team_a = self.team) & Q(players_a__id = self.player.id) ).distinct().count()
                ngames += regular.gamematch_set.filter(Q(team_b = self.team) & Q(players_b__id = self.player.id) ).distinct().count()
                
                games = list()
                games += regular.gamematch_set.filter(Q(team_a = self.team)).distinct()
                games += regular.gamematch_set.filter(Q(team_b = self.team)).distinct()
                nmiss += self.player.gamematchgoal_miss.filter(gamematch__in = games).count()
                #print "\n\n\n\nNmiss2\n\n\n\n\n\n"
                #print nmiss
                nfines += self.player.gamematchfine_set.filter(team = self.team, gamematch__in = games).count()
                fines += sum(fine.minutes for fine in self.player.gamematchfine_set.filter(team = self.team, gamematch__in = games))
                
                assistant_count = len(GameMatchGoal.objects.filter(Q(assistant_1 = self.player) | Q(assistant_2 = self.player), gamematch__in = games).distinct())
                # there isn't two same assistant
                ntrans += assistant_count
                ntrans += self.player.gamematchgoal_trans.filter(team = self.team, gamematch__in = games).count()
                
                goalminutes += sum([ gtime.get_diff_minute()
                    for gtime in self.player.gamematchgtime_set.filter(player=self.player, gamematch__in = games).distinct()
                ]) / 2
                
                ngoals += GameMatchGoal.objects.filter(goal_player=self.player, gamematch__in = games).distinct().count()
            
            player2stat.playerstat.ngames = ngames
            player2stat.playerstat.ngoals = ngoals
            player2stat.playerstat.nmisses = nmiss
            player2stat.playerstat.nfines = nfines
            player2stat.playerstat.nfines_minutes = fines
            player2stat.playerstat.ntrans = ntrans
            player2stat.playerstat.goalminutes = goalminutes
            player2stat.playerstat.ngoalsntrans = player2stat.playerstat.ngoals + player2stat.playerstat.ntrans
            player2stat.playerstat.safety_factor = self.get_safety_factor(player2stat.playerstat, season)
            
                        
            player2stat.playerstat.save()
            #print "%s [%s %s] match_count %d: %d %d" % ( self.team.name, self.player.first_name, self.player.second_name,  player2stat.playerstat.ngames, player2stat.id, ngoals )
        pass
        #self.query_set = self.get_division_query()
        #self.season_games = GameMatch.objects.filter(self.query_set).distinct()
        #self.ngoals = self.get_ngoals()
        #self.nmisses =  self.get_nmisses()

        #self.ntrans = self.get_ntrans()
        #self.nfines = self.get_nfines()
        #self.nfines_minutes = self.get_nfines_minutes()
        #self.ngames = self.get_ngames()
        #self.goalminutes = self.get_goalminutes()

        #self.safety_factor =  self.get_safety_factor()

        #self.ngoalsntrans = self.ngoals + self.ntrans

    def __unicode__(self):
        return u"%s, %s"%(self.game_number, self.player.second_name)

    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока: команду"
        verbose_name_plural = "игроки: команды"
