# -*- coding: utf-8 -*-

from django.contrib import admin

from django.db.models import Q


from grizzly.models import JudgeType
from grizzly.models import Judge
from grizzly.models import InsuranceType
from grizzly.models import PlayerType
from grizzly.models import PlayerStatus
from grizzly.models import Player
from grizzly.models import Player2Team
from grizzly.models import PlayerStat
from grizzly.models import Player2Stat
from grizzly.models import Trainer
from grizzly.models import Rink
from grizzly.models import RinkSchedule
from grizzly.models import Team
from grizzly.models import TeamSchedule
from grizzly.models import TeamPlugin
from grizzly.models import Training
from grizzly.models import GameSeason
from grizzly.models import GameDivision
from grizzly.models import GameTournamentFormat
from grizzly.models import GameTournamentSystem
from grizzly.models import GameTournamentRegular

from grizzly.models import GameTournamentPlayOff

from grizzly.models import GameMatch

from grizzly.models import GameMatch
from grizzly.models import GameMatchGoal
from grizzly.models import GameFineType
from grizzly.models import GameMatchFine
from grizzly.models import GameMatchGTime
from grizzly.models import GameMatchPenalty


from grizzly.models import FinalType


from absbuttonablemodeladmin import AbsButtonableModelAdmin

from absobjadmin import AbsObjAdmin
from abspersadmin import AbsPersAdmin


from absobjadmin import AbsObjTabularInline

class FinalTypeAdmin(AbsObjAdmin):
    pass


class JudgeTypeAdmin(AbsObjAdmin):
    pass

class InsuranceTypeAdmin(AbsObjAdmin):
    pass


class PlayerTypeAdmin(AbsObjAdmin):
    pass


class PlayerStatusAdmin(AbsObjAdmin):
    pass

class JudgeAdmin(AbsPersAdmin):
    filter_horizontal = (
        'types',
    )



class Player2TeamAdminInline(AbsObjTabularInline):
    readonly_fields = (
        'ngames',
        'ngoals',
        'nfines',
        'ntrans',
        'npoints',
    )
    model = Player2Team
    exclude = ('description', 'detail', 'name')


class PlayerAdmin(AbsPersAdmin):
    exclude = ['gamematchgoal_trans']

    inlines = [
        Player2TeamAdminInline,
    ]



class TrainerAdmin(AbsPersAdmin):
    pass


class RinkScheduleAdmin(AbsObjAdmin):
    pass


class RinkAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'town',
        'street',
        'house',
        'building'
    )
    list_filter = (
        'town',
        'street'
    )
    search_fields = (
        'name',
        'town',
        'street',
        'house',
        'building'
    )
    filter_horizontal = ('rinkschedules',)

class TeamScheduleAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'start_date',
        'stop_date',
        'start_time',
        'stop_time'
    )
    list_filter = tuple()
    search_fields = (
        'name',
        'start_date',
        'stop_date',
        'start_time',
        'stop_time'
    )
    filter_horizontal = ('teams',)


class PlayerStatAdmin(AbsObjAdmin):
    list_display = (
        'season',
        'ngames',
    )

class Player2StatAdmin(AbsObjAdmin):
    list_display = (
        'player2team',
        'playerstat',
    )
    exclude = (
        'description',
        'detail',
        'image',
        'name',
    )

class Player2TeamAdmin(AbsObjAdmin):
    list_display = (
        'player',
        'team',
    )

class TeamAdmin(AbsObjAdmin):
    readonly_fields = (
        'ngames',
        'nwins',
        'ndraws',
        'nloses',
        'ngoals',
        'nmisses',
        'npoints',
    )

    list_display = (
        'id',
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )
    filter_horizontal = (
        'teamschedules',
        'gamedivisions'
    )
    inlines = [
        Player2TeamAdminInline,
    ]

class TeamPluginAdmin(AbsObjAdmin):
    pass

class TrainingAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'team',
        'rink',
        'trainer'
    )
    list_filter = tuple()
    search_fields = (
        'name',
        'description'
    )


class GameSeasonAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'start_datetime',
        'stop_datetime',
    )
    list_filter = tuple()
    search_fields = (
        'name',
        'start_datetime',
        'stop_datetime',
    )
    filter_horizontal = (
        'gamedivisions',
    )


class GameDivisionAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'start_datetime',
        'stop_datetime',
    )
    search_fields = (
        'name',
        'start_datetime',
        'stop_datetime',
    )
    filter_horizontal = (
        'gameseasons',
        'teams'
    )

class GameTournamentFormatAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )

class GameTournamentSystemAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )

class GameMatchGoalAdminInline(AbsObjTabularInline):
    model = GameMatchGoal
    exclude = ('description', 'detail', 'image', 'name', 'trans_players')


    readonly_fields = ('goal_keeper',)


    related_search_fields = {
        'team': ('name',),
        'gamematch': {
            'fields': ('name', 'rink__name', 'team_a__name', 'team_b__name'),
            'format': u"%s (%s): «%s» × «%s»"
        },
        'goal_player': {
            'fields': ('game_number', 'second_name', 'first_name', 'patronymic',),
            'format': u"%s, %s %s %s"
        },
        'trans_players': {
            'fields': ('game_number', 'second_name', 'first_name', 'patronymic',),
            'format': u"%s, %s %s %s"
        }
    }

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(GameMatchGoalAdminInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )
        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'team':
                field.queryset = field.queryset.filter(
                    id__in = (request._obj_.team_a.id, request._obj_.team_b.id)
                )
            if db_field.name == 'goal_player':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )
            if db_field.name == 'assistant_1' or db_field.name == 'assistant_2':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )
        return field




class GameMatchFineAdminInline(AbsObjTabularInline):
    model = GameMatchFine
    exclude = ('description', 'detail', 'image', 'name')

    related_search_fields = {
        'team': ('name',),
        'gamematch': {
            'fields': ('name', 'rink__name', 'team_a__name', 'team_b__name'),
            'format': u"%s (%s): «%s» × «%s»"
        },
        'fine_player': {
            'fields': ('game_number', 'second_name', 'first_name', 'patronymic',),
            'format': u"%s, %s %s %s"
        }
    }

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(GameMatchFineAdminInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'team':
                field.queryset = field.queryset.filter(
                    id__in = (request._obj_.team_a.id, request._obj_.team_b.id)
                )
            if db_field.name == 'fine_player':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )
        return field


class GameMatchGTimeAdminInline(AbsObjTabularInline):
    model = GameMatchGTime
    exclude = ('description', 'detail', 'image', 'name', 'a', 'b')
    readonly_fields = ('start_minute','start_second','stop_minute','stop_second')


    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(GameMatchGTimeAdminInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'team':
                field.queryset = field.queryset.filter(
                    id__in = (request._obj_.team_a.id, request._obj_.team_b.id)
                )
            if db_field.name == 'player':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )
        return field



class GameMatchPenaltyAdminInline(AbsObjTabularInline):
    model = GameMatchPenalty
    exclude = ('description', 'detail', 'image', 'name', 'a', 'b', 'gla', 'glb')

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(GameMatchPenaltyAdminInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'team':
                field.queryset = field.queryset.filter(
                    id__in = (request._obj_.team_a.id, request._obj_.team_b.id)
                )
            if db_field.name == 'player':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )
            if db_field.name == 'gl_player':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a, request._obj_.team_b)
                )

        return field


class GameMatchAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'rink',
        'team_a',
        'team_b',
    )
    list_filter = (
        'team_a',
        'team_b',
    )
    search_fields = (
        'name',
        'rink',
        'team_a',
        'team_b',
    )
    filter_horizontal = (
        'judges',
        'players_a',
        'players_b',
    )

    inlines = [
        GameMatchGoalAdminInline,
        GameMatchFineAdminInline,
        GameMatchGTimeAdminInline,
        GameMatchPenaltyAdminInline
    ]


    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(GameMatchAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(GameMatchAdmin, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )
        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'best_player_a':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_a,)
                )
            if db_field.name == 'best_player_b':
                field.queryset = field.queryset.filter(
                    teams__in = (request._obj_.team_b,)
                )
        return field
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        field = super(GameMatchAdmin, self).formfield_for_manytomany(
            db_field,
            request,
            **kwargs
        )

        if request._obj_ and request._obj_.team_a :
            if db_field.name == 'players_a':
                pids = [p.id for p in request._obj_.team_a.player2team_set.all()]
                field.queryset = field.queryset.filter(player2team__in = pids)

        if request._obj_ and request._obj_.team_b :
            if db_field.name == 'players_b':
                pids = [p.id for p in request._obj_.team_b.player2team_set.all()]
                field.queryset = field.queryset.filter(player2team__in = pids)

        return field

class GameMatchGoalAdmin(AbsObjAdmin):


    related_search_fields = {
        'team': ('name',),
        'gamematch': {
            'fields': ('name', 'rink__name', 'team_a__name', 'team_b__name'),
            'format': u"%s (%s): «%s» × «%s»"
        },
        'goal_player': {
            'fields': ('game_number', 'second_name', 'first_name', 'patronymic',),
            'format': u"%s, %s %s %s"
        }
    }


    filter_horizontal = (
        'trans_players',
    )

    list_display = (
        'id',
        'team',
        'goalno',
        'gamematch',
        'goal_player',
        'game_situation'
    )
    list_filter = (
        'team',
        'gamematch',
        'goal_player',
    )
    search_fields = (
        'team',
        'goalno',
        'gamematch',
        'goal_player',
        'game_situation'
    )





class GameMatchGTimeAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'gamematch'
    )
    list_filter = tuple()
    search_fields = (
        'gamematch',
    )

class GameMatchPenaltyAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'gamematch',
        'a',
        'b',
        'gla',
        'glb',
        'result'
    )
    list_filter = tuple()
    search_fields = (
        'gamematch'
        'a',
        'b',
        'gla',
        'glb',
        'result'
    )


class GameFineTypeAdmin(AbsObjAdmin):
    pass

class GameMatchFineAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'gamematch',
        'team',
        'start_time',
        'stop_time',
        'fine_player',
        'type',
    )
    list_filter = tuple()
    search_fields = (
        'gamematch',
        'team',
        'start_time',
        'stop_time',
        'fine_player',
        'type',
    )


class GameMatchAdminInlineR(AbsObjTabularInline):
    model = GameMatch
    exclude = (
        'description',
        'detail',
        'image',
        'name',
        'stop_datetime',
        'gametournamentplayoff',
        'finaltype',
        'players_a',
        'players_b',
        'best_player_a',
        'best_player_b'
    )
    
    list_display = (
        'id',
        'name',
        'rink',
        'team_a',
        'team_b',
    )
    
    list_filter = (
        'team_a',
        'team_b',
    )


class GameMatchAdminInlineP(AbsObjTabularInline):
    model = GameMatch
    exclude = (
        'description',
        'detail',
        'image',
        'name',
        'stop_datetime',
        'gametournamentregular',
        'tourno',
        'players_a',
        'players_b',
        'best_player_a',
        'best_player_b'
    )


class GameTournamentRegularAdmin(AbsButtonableModelAdmin, AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'start_datetime',
        'stop_datetime',
    )


    list_filter = tuple()

    search_fields = (
        'id',
        'name',
        'description',
        'start_datetime',
        'stop_datetime',
    )
    filter_horizontal = (
        'teams',
        'gamedivisions',
    )

    buttons = [
        ('build_matrix', "Посчитать матрицу игр")
    ]

    inlines = [
        GameMatchAdminInlineR,
    ]

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(GameTournamentRegularAdmin, self).get_form(request, obj, **kwargs)
    
    def build_matrix(self, request, tournament):
        '''
            Генерации матрицы игр
            Простой, не эффективный и не очень устойчивый алгоритм.
            http://thiswap.com/2011/07/21/algoritm-sostavleniya-raspisaniya-sportivnyx-matchej/
        '''
        teams_list = [team for team in tournament.teams.all()];
        teams_list = sorted(teams_list, key=lambda x: x.id)
        all_team = len(teams_list)

        if (all_team % 2):
            all_team += 1;

        teams_list.append(None);
        k = all_team / 2

        S = {}
        for tourno in xrange(1, all_team):
            team2 = teams_list[2-1]
            for y in xrange(2, all_team):
                teams_list[y-1] = teams_list[y]
            teams_list[all_team-1] = team2;

            for j in xrange(1, k + 1):
                x = j
                y = all_team - j + 1
                team_a = teams_list[x-1]
                team_b = teams_list[y-1]
                cnt = GameMatch.objects.filter(
                    tourno = tourno,
                    team_a = team_a,
                    team_b = team_b,
                    gametournamentregular = tournament
                ).count()
                if (0 == cnt and team_a and team_b):
                    name =  u"%s (%d): «%s» × «%s»"%(tournament.name, tourno, team_a.name, team_b.name)
                    gm = GameMatch(
                        tourno = tourno,
                        name = name,
                        team_a = team_a,
                        team_b = team_b,
                        gametournamentregular = tournament
                    );
                    gm.save()

                if not(team_a):
                    team_a = lambda: 0
                    team_a.id = 0;

                if not(team_b):
                    team_b = lambda: 0
                    team_b.id = 0;

                print tourno, team_a.id, team_b.id


                if S.get(team_a.id, None) == None:
                     S[team_a.id] = {}

                if S.get(team_b.id, None) == None:
                     S[team_b.id] = {}

                S[team_a.id][tourno] = team_b.id
                S[team_b.id][tourno] = team_a.id

        for x in S:
            print x, "|",
            for y in S[x]:
                print "%s "%(S[x][y]),
            print

    def build_matrix_1(self, request, tournament):
        '''
            Генерации матрицы игр.
            Потенциально устойчивый алгоритм, основанный на сдвигах.
            http://otvet.mail.ru/question/57757993
            Довести до конца не удалось.
        '''
        teams_list = [team for team in tournament.teams.all()];
        teams_list = sorted(teams_list, key=lambda x: x.id)
        teams_len = len(teams_list)
        xl = teams_len
        odd = teams_len % 2
        #if (odd):
        teams_len += 1
        S = {}
        for i in xrange(0, teams_len-1):
            xteams_list = []

            if (odd):
                xteams_list.append(None)
            else:
                xteams_list.append(teams_list[xl-1])

            for j in xrange(xl):
                xteams_list += [teams_list[(j + i) % (xl)]]
            print xteams_list
            for t1 in xrange(0, teams_len/2):
                x = t1
                y = teams_len - t1 - 1
                team_a = xteams_list[x]
                team_b = xteams_list[y]
                tourno = i + 1
                if (not team_a):
                    team_a = lambda:0
                    team_a.id = 0
                if (not team_b):
                    team_b = lambda:0
                    team_b.id = 0
                if S.get(team_a.id, None) == None:
                     S[team_a.id] = {}
                if S.get(team_b.id, None) == None:
                     S[team_b.id] = {}
                S[team_a.id][tourno] = team_b.id
                S[team_b.id][tourno] = team_a.id

        for x in S:
            print x, "|",
            for y in S[x]:
                print "%s "%(S[x][y]),
            print


    def build_matrix_2(self, request, tournament):
        '''
            Генерации матрицы игр
            Алгоритм основанный на сумме чисел.
            Должен быть устойчивым.
            Довести до конца не удалось.
                http://www.bcc.h14.ru/guestbook.php
                Сообщение №64.
        '''
        teams_list = [team for team in tournament.teams.all()];
        teams_list = sorted(teams_list, key=lambda x: x.id)
        teams_len = len(teams_list)
        if (teams_len % 2):
            xteams_list.append(None)
        S = {}
        for i in xrange(1, teams_len + 1):
            for j in xrange(1, teams_len + 1):
                if(i != j):
                    s = (i + j - 1)
                    if s > teams_len:
                        s = (s - teams_len)
                        print '>', s, i, j

                    elif (s < teams_len):
                        s = s - 1
                        print '<', s, i, j
                    else:
                        print '=', s, i, j

                    if S.get(i, None):
                        S[i][s] = j
                    else:
                        S[i] = {s: j}
            print




class GameTournamentPlayOffAdmin(AbsObjAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'start_datetime',
        'stop_datetime',
    )


    list_filter = tuple()

    search_fields = (
        'id',
        'name',
        'description',
        'start_datetime',
        'stop_datetime',
    )
    filter_horizontal = (
        'teams',
        'gamedivisions',
    )

    inlines = [
        GameMatchAdminInlineP,
    ]


class Player2TeamMeta(Player2Team):
    class Meta:
        proxy = True
        verbose_name = "Игры: дисквалифицированный игрок"
        verbose_name_plural = "Игры: дисквалифицированные игроки"

class Player2TeamAdminFiltered(Player2TeamAdmin):
    def queryset(self, request):
        return self.model.objects.filter(is_disqualified = True)


admin.site.register(FinalType, FinalTypeAdmin)
admin.site.register(JudgeType, JudgeTypeAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(InsuranceType, InsuranceTypeAdmin)

##
## Игроки
##
admin.site.register(PlayerType,     PlayerTypeAdmin)
admin.site.register(PlayerStatus,   PlayerStatusAdmin)
admin.site.register(Player,         PlayerAdmin)
admin.site.register(Player2Team,    Player2TeamAdmin)
admin.site.register(PlayerStat,     PlayerStatAdmin)
admin.site.register(Player2Stat,    Player2StatAdmin)
admin.site.register(Player2TeamMeta,    Player2TeamAdminFiltered)


admin.site.register(Trainer, TrainerAdmin)

admin.site.register(Rink,           RinkAdmin)
admin.site.register(RinkSchedule,   RinkScheduleAdmin)

##
## Команды
##
admin.site.register(Team,           TeamAdmin)
admin.site.register(TeamSchedule,   TeamScheduleAdmin)

admin.site.register(Training, TrainingAdmin)

##
## Игровая логика
##
admin.site.register(GameSeason,             GameSeasonAdmin)
admin.site.register(GameDivision,           GameDivisionAdmin)

admin.site.register(GameTournamentRegular,  GameTournamentRegularAdmin)

admin.site.register(GameTournamentPlayOff,  GameTournamentPlayOffAdmin)


admin.site.register(GameTournamentSystem,   GameTournamentSystemAdmin)
admin.site.register(GameTournamentFormat,   GameTournamentFormatAdmin)

admin.site.register(GameMatch,          GameMatchAdmin)
admin.site.register(GameMatchGoal,      GameMatchGoalAdmin)
admin.site.register(GameFineType,       GameFineTypeAdmin)
admin.site.register(GameMatchFine,      GameMatchFineAdmin)
admin.site.register(GameMatchGTime,     GameMatchGTimeAdmin)
admin.site.register(GameMatchPenalty,   GameMatchPenaltyAdmin)





