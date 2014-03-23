# -*- coding: utf-8 -*-

from django.contrib import admin


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


class GameMatchGoalAdmin(AbsObjAdmin):
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
        'a',
        'b',
        'time'
    )
    list_filter = tuple()
    search_fields = (
        'a',
        'b',
        'time'
    )

class GameMatchPenaltyAdmin(AbsObjAdmin):
    list_display = (
        'a',
        'b',
        'gla',
        'glb',
        'result'
    )
    list_filter = tuple()
    search_fields = (
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





