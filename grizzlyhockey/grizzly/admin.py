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
from grizzly.models import GameTournament

from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin

class JudgeTypeAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

class JudgeAdmin(PlaceholderAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic')
    list_filter = []
    search_fields = ( 'second_name', 'first_name', 'patronymic')
    filter_horizontal = ('types',)


class InsuranceTypeAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

class PlayerTypeAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

class PlayerStatusAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

class PlayerAdmin(PlaceholderAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic', 'game_number', 'role')
    list_filter = ('role', 'game_number', 'status')
    search_fields = ( 'second_name', 'first_name', 'patronymic', 'game_number', 'role')


class TrainerAdmin(PlaceholderAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic')
    list_filter = []
    search_fields = ( 'second_name', 'first_name', 'patronymic')

class RinkScheduleAdmin(PlaceholderAdmin):
    list_display = ('name', 'description', 'start_date', 'stop_date', 'start_time', 'stop_time')
    list_filter = []
    search_fields = ('name', 'description', 'start_date', 'stop_date', 'start_time', 'stop_time')
    filter_horizontal = ('rinks',)


class RinkAdmin(ModelAdminWithTabsAndCMSPlaceholder):
    list_display = ('name', 'town', 'description', 'street', 'house', 'building')
    list_filter = ('town', 'street')
    search_fields = ('name','town', 'description', 'street', 'house', 'building')
    filter_horizontal = ('rinkschedules',)

    address_fieldsets = (('', {'fields': ('name', 'town', 'street', 'house', 'building', 'birthday', 'rinkschedules'),}),)

    description_fieldsets = (('', {
        'fields': ('description',),

    }),)

    tabs = (
        ('Address', {'fieldsets': address_fieldsets,}),
        ('Description', {'fieldsets': description_fieldsets,}),
    )


    #description_fieldsets = (('', {
        #'fields': ('description',),
        #'classes': ('plugin-holder', 'plugin-holder-nopage'),
        #}),)

class TeamScheduleAdmin(PlaceholderAdmin):
    list_display = ('name', 'description', 'start_date', 'stop_date', 'start_time', 'stop_time')
    list_filter = []
    search_fields = ('name', 'description', 'start_date', 'stop_date', 'start_time', 'stop_time')
    filter_horizontal = ('teams',)



class TeamAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = []
    search_fields = ('name', 'description')
    filter_horizontal = ('players', 'teamschedules')

class TeamPluginAdmin(PlaceholderAdmin):
    pass

class TrainingAdmin(PlaceholderAdmin):
    list_display = ('name', 'description', 'team', 'rink', 'trainer')
    list_filter = []
    search_fields = ('name', 'description')




class GameSeasonAdmin(PlaceholderAdmin):
    list_display = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    list_filter = []
    search_fields = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )

class GameDivisionAdmin(PlaceholderAdmin):
    list_display = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time',
        'gameseason'
    )
    list_filter = ('gameseason',)
    search_fields = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )

class GameTournamentFormatAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = []
    search_fields = ('name', 'description')

class GameTournamentSystemAdmin(PlaceholderAdmin):
    list_display = ('name', 'description')
    list_filter = []
    search_fields = ('name', 'description')


class GameTournamentAdmin(PlaceholderAdmin):
    list_display = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time',
        'gametournamentformat',
        'gametournamentsystem',
    )
    
    list_filter = (
        'gametournamentformat',
        'gametournamentsystem'
    )

    search_fields = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    filter_horizontal = ('teams',)

admin.site.register(JudgeType, JudgeTypeAdmin)
admin.site.register(Judge, JudgeAdmin)

admin.site.register(InsuranceType, InsuranceTypeAdmin)

admin.site.register(PlayerType,     PlayerTypeAdmin)
admin.site.register(PlayerStatus,   PlayerStatusAdmin)
admin.site.register(Player,         PlayerAdmin)

admin.site.register(Trainer, TrainerAdmin)

admin.site.register(Rink,           RinkAdmin)
admin.site.register(RinkSchedule,   RinkScheduleAdmin)

admin.site.register(Team,           TeamAdmin)
admin.site.register(TeamSchedule,   TeamScheduleAdmin)

admin.site.register(Training, TrainingAdmin)

admin.site.register(GameSeason,             GameSeasonAdmin)
admin.site.register(GameDivision,           GameDivisionAdmin)
admin.site.register(GameTournament,         GameTournamentAdmin)
admin.site.register(GameTournamentSystem,   GameTournamentSystemAdmin)
admin.site.register(GameTournamentFormat,   GameTournamentFormatAdmin)


