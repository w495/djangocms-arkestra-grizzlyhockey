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
from django.http import HttpResponseRedirect, HttpResponse
from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin


class ButtonableModelAdmin(admin.ModelAdmin):
    '''
        Миксин, добавляет новые действия (кнопки)
        к стандартным действиям админки.
        После выполнения действия переходит на предыдущую ссылку.
        В наследуемом классе должен быть определен атрибут
            buttons = [
                ('<action1>', <action1 description>)
                ('<action2>', <action2 description>)
                ...
            ]
        И соответствующие функции:
        def <action1>(self, request, obj):
            ...
        def <action2>(self, request, obj):
            ...
    '''

    def change_view(self, request, object_id, extra_context={}):
        extra_context['buttons'] = self.buttons
        return super(ButtonableModelAdmin, self).change_view(
                request=request, object_id=object_id, extra_context=extra_context)

    def button_view_dispatcher(self, request, object_id, command):
        obj = self.model._default_manager.get(pk=object_id)
        return getattr(self, command)(request, obj) \
                or HttpResponseRedirect(request.META['HTTP_REFERER'])

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url
        from django.utils.functional import update_wrapper
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        return patterns('',
            *(url(r'^(\d+)/(%s)/$' % but[0], wrap(self.button_view_dispatcher)) for but in self.buttons)
        ) + super(ButtonableModelAdmin, self).get_urls()




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
    filter_horizontal = ('teams',)

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
    filter_horizontal = ('players', 'teamschedules', 'gamedivisions')

class TeamPluginAdmin(PlaceholderAdmin):
    pass

class TrainingAdmin(PlaceholderAdmin):
    list_display = ('name', 'description', 'team', 'rink', 'trainer')
    list_filter = []
    search_fields = ('name', 'description')


class GameSeasonAdmin(PlaceholderAdmin):
    list_display = (
        'name',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    list_filter = []
    search_fields = (
        'name',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    filter_horizontal = ('gamedivisions', )


class GameDivisionAdmin(PlaceholderAdmin):
    list_display = (
        'name',
        'start_date', 'stop_date',
        'start_time', 'stop_time',
    )
    search_fields = (
        'name',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    filter_horizontal = ('gameseasons', 'teams')

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



def make_publishedx(modeladmin, request, queryset):
    print ("x")

make_publishedx.short_description = "X"


class GameTournamentRegularAdmin(PlaceholderAdmin, ButtonableModelAdmin):
    list_display = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time',
    )

    list_filter = []

    search_fields = (
        'name',
        'description',
        'start_date', 'stop_date',
        'start_time', 'stop_time'
    )
    filter_horizontal = ('teams',)

    actions = [make_publishedx]

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

            xteams_list = []
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


