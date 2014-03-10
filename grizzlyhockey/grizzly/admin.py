from django.contrib import admin



from grizzly.models import JudgeType
from grizzly.models import Judge

from grizzly.models import InsuranceType
from grizzly.models import PlayerType
from grizzly.models import PlayerStatus
from grizzly.models import Player

from grizzly.models import Trainer

from grizzly.models import Rink
from grizzly.models import Team
from grizzly.models import Training

class JudgeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']

class JudgeAdmin(admin.ModelAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic')
    list_filter = []
    search_fields = [ 'second_name', 'first_name', 'patronymic']
    filter_horizontal = ('types',)


class InsuranceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']

class PlayerTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']

class PlayerStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic', 'game_number', 'role')
    list_filter = ['role', 'game_number', 'status']
    search_fields = [ 'second_name', 'first_name', 'patronymic', 'game_number', 'role']


class TrainerAdmin(admin.ModelAdmin):
    list_display = ( 'second_name', 'first_name', 'patronymic')
    list_filter = []
    search_fields = [ 'second_name', 'first_name', 'patronymic']

class RinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'town', 'street', 'house', 'building')
    list_filter = ['town', 'street']
    search_fields = ['name', 'description', 'town', 'street', 'house', 'building']

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = []
    search_fields = ['name', 'description']
    filter_horizontal = ('players',)


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'team', 'rink', 'trainer')
    list_filter = []
    search_fields = ['name', 'description']


admin.site.register(JudgeType, JudgeTypeAdmin)
admin.site.register(Judge, JudgeAdmin)

admin.site.register(InsuranceType, InsuranceTypeAdmin)
admin.site.register(PlayerType, PlayerTypeAdmin)
admin.site.register(PlayerStatus, PlayerStatusAdmin)
admin.site.register(Player, PlayerAdmin)

admin.site.register(Trainer, TrainerAdmin)

admin.site.register(Rink, RinkAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Training, TrainingAdmin)
