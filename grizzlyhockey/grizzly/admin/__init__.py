# -*- coding: utf-8 -*-

from django.contrib import admin

from django.db.models import Q


from grizzly.models import JudgeType
from grizzly.models import Judge
from grizzly.models import InsuranceType
from grizzly.models import PlayerType
from grizzly.models import PlayerStatus
from grizzly.models import Player
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
from grizzly.models import GameMatch

from grizzly.models import GameMatch
from grizzly.models import GameMatchGoal
from grizzly.models import GameFineType
from grizzly.models import GameMatchFine
from grizzly.models import GameMatchGTime
from grizzly.models import GameMatchPenalty



from absbuttonablemodeladmin import AbsButtonableModelAdmin

from absobjadmin import AbsObjAdmin
from abspersadmin import AbsPersAdmin


from absobjadmin import AbsObjTabularInline


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


class PlayerAdmin(AbsPersAdmin):
    filter_horizontal = (
        'teams',
    )


class TrainerAdmin(AbsPersAdmin):
    pass


class RinkScheduleAdmin(AbsObjAdmin):
    pass


class RinkAdmin(AbsObjAdmin):
    list_display = (
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



class TeamAdmin(AbsObjAdmin):
    list_display = (
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )
    filter_horizontal = (
        'players',
        'teamschedules',
        'gamedivisions'
    )

class TeamPluginAdmin(AbsObjAdmin):
    pass

class TrainingAdmin(AbsObjAdmin):
    list_display = (
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
    filter_horizontal = (
        'gamedivisions',
    )


class GameDivisionAdmin(AbsObjAdmin):
    list_display = (
        'name',
        'start_date',
        'stop_date',
        'start_time',
        'stop_time',
    )
    search_fields = (
        'name',
        'start_date',
        'stop_date',
        'start_time',
        'stop_time'
    )
    filter_horizontal = (
        'gameseasons',
        'teams'
    )

class GameTournamentFormatAdmin(AbsObjAdmin):
    list_display = (
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )

class GameTournamentSystemAdmin(AbsObjAdmin):
    list_display = (
        'name',
    )
    list_filter = tuple()
    search_fields = (
        'name',
    )

class GameMatchGoalAdminInline(AbsObjTabularInline):
    model = GameMatchGoal
    exclude = ('description', 'detail', 'image', 'name')

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
        return field


    def formfield_for_manytomany(self, db_field, request, **kwargs):
        field = super(GameMatchGoalAdminInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )
        if request._obj_ and request._obj_.team_a and request._obj_.team_b:
            if db_field.name == 'trans_players':
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
    exclude = ('description', 'detail', 'image', 'name')


class GameMatchPenaltyAdminInline(AbsObjTabularInline):
    model = GameMatchPenalty
    exclude = ('description', 'detail', 'image', 'name')



class GameMatchAdmin(AbsObjAdmin):
    list_display = (
        'name',
        'rink',
        'team_a',
        'team_b',
    )
    list_filter = tuple()
    search_fields = (
        'name',
        'rink',
        'team_a',
        'team_b',
    )
    filter_horizontal = (
        'judges',
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
        'team',
        'time',
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
        'time',
        'goalno',
        'gamematch',
        'goal_player',
        'game_situation'
    )





class GameMatchGTimeAdmin(AbsObjAdmin):
    list_display = (
        'gamematch',
        'a',
        'b',
        'time'
    )
    list_filter = tuple()
    search_fields = (
        'gamematch'
        'a',
        'b',
        'time'
    )

class GameMatchPenaltyAdmin(AbsObjAdmin):
    list_display = (
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




class GameTournamentRegularAdmin(AbsObjAdmin, AbsButtonableModelAdmin):
    list_display = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time',
    )

    list_filter = tuple()

    search_fields = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    filter_horizontal = (
        'teams',
        'gamedivisions',
    )

    buttons = [
        ('build_matrix', "Посчитать матрицу игр")
    ]

    def build_matrix(self, request, tournament):
        '''
            Генерации матрицы игр
        '''
        teams_list = [team for team in tournament.teams.all()];
        teams_len = len(teams_list)

        games_len = teams_len




        print
        print
        print
        print

        if (teams_len % 2):
            games_len += 1

        for i in xrange(games_len):

            xteams_list = tuple()
            for j in xrange(teams_len):
                xteams_list += [teams_list[(j + i) % teams_len]]

            if (teams_len % 2):
                xteams_list.append(None)

            print xteams_list
            for t1 in xrange(0, games_len, 2):
                print i + 1, xteams_list[t1], xteams_list[t1 + 1]


        print
        print
        print
        print




admin.site.register(JudgeType, JudgeTypeAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(InsuranceType, InsuranceTypeAdmin)

##
## Игроки
##
admin.site.register(PlayerType,     PlayerTypeAdmin)
admin.site.register(PlayerStatus,   PlayerStatusAdmin)
admin.site.register(Player,         PlayerAdmin)

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

admin.site.register(GameTournamentSystem,   GameTournamentSystemAdmin)
admin.site.register(GameTournamentFormat,   GameTournamentFormatAdmin)

admin.site.register(GameMatch,          GameMatchAdmin)
admin.site.register(GameMatchGoal,      GameMatchGoalAdmin)
admin.site.register(GameFineType,       GameFineTypeAdmin)
admin.site.register(GameMatchFine,      GameMatchFineAdmin)
admin.site.register(GameMatchGTime,     GameMatchGTimeAdmin)
admin.site.register(GameMatchPenalty,   GameMatchPenaltyAdmin)





