from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from django.core.paginator import Paginator

from grizzly.models import PlayerType
from grizzly.models import Player
from grizzly.models import PlayerPlugin
from grizzly.models import JudgeType
from grizzly.models import Judge
from grizzly.models import Trainer
from grizzly.models import Rink
from grizzly.models import Team
from grizzly.models import RinkSchedule
from grizzly.models import TeamSchedule
from grizzly.models import TeamPlugin
from grizzly.models import TeamPluginMany
from grizzly.models import Training
from grizzly.models import GameSeason
from grizzly.models import GameSeasonPlugin
from grizzly.models import GameSeasonPluginMany
from grizzly.models import GameDivision
from grizzly.models import GameDivisionPlugin
from grizzly.models import GameDivisionPluginMany
from grizzly.models import GameTournamentFormat
from grizzly.models import GameTournamentSystem
from grizzly.models import GameTournamentRegular
from grizzly.models import GameTournamentPlayOff

from grizzly.models import GameTournamentRegularPlugin
from grizzly.models import GameTournamentRegularPluginMany
from grizzly.models import GameMatch
from grizzly.models import GameMatchPlugin
from grizzly.models import GameMatchPluginMany
from grizzly.models import GameMatchGoal
from grizzly.models import GameFineType
from grizzly.models import GameMatchFine
from grizzly.models import GameMatchGTime
from grizzly.models import GameMatchPenalty
from grizzly.models import InsuranceType
from grizzly.models import PlayerStatus


import datetime

class GameDivisionListView(generic.ListView):
    model = GameDivision
    template_name = 'grizzly/pages/game-division-list.html'

class GameDivisionDetailView(generic.DetailView):
    model = GameDivision
    template_name = 'grizzly/pages/game-division-detail.html'


class GameMatchFineListView(generic.ListView):
    model = GameMatchFine
    template_name = 'grizzly/pages/game-match-fine-list.html'

class GameMatchFineDetailView(generic.DetailView):
    model = GameMatchFine
    template_name = 'grizzly/pages/game-match-fine-detail.html'



class GameMatchGoalListView(generic.ListView):
    model = GameMatchGoal
    template_name = 'grizzly/pages/game-match-goal-list.html'

class GameMatchGoalDetailView(generic.DetailView):
    model = GameMatchGoal
    template_name = 'grizzly/pages/game-match-goal-detail.html'



class GameMatchGTimeListView(generic.ListView):
    model = GameMatchGTime
    template_name = 'grizzly/pages/game-match-gtime-list.html'

class GameMatchGTimeDetailView(generic.DetailView):
    model = GameMatchGTime
    template_name = 'grizzly/pages/game-match-gtime-detail.html'



class GameMatchPenaltyListView(generic.ListView):
    model = GameMatchPenalty
    template_name = 'grizzly/pages/game-match-penalty-list.html'

class GameMatchPenaltyDetailView(generic.DetailView):
    model = GameMatchPenalty
    template_name = 'grizzly/pages/game-match-penalty-detail.html'




class GameMatchListView(generic.ListView):
    model = GameMatch
    template_name = 'grizzly/pages/game-match-list.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().order_by('-start_datetime')

class GameMatchDetailView(generic.DetailView):
    model = GameMatch
    template_name = 'grizzly/pages/game-match-detail.html'


class GameMatchScheduleView(generic.ListView):
    model = GameMatch
    template_name = 'grizzly/pages/game-match-schedule.html'

    def get_queryset(self, *args, **kwargs):
        date = datetime.date.today()
        end_week = date + datetime.timedelta(10)
        return self.model.objects.filter(
            start_datetime__gt = date
        ).order_by('start_datetime')




class GameSeasonListView(generic.ListView):
    model = GameSeason
    template_name = 'grizzly/pages/game-season-list.html'

class GameSeasonDetailView(generic.DetailView):
    model = GameSeason
    template_name = 'grizzly/pages/game-season-detail.html'



class GameTournamentRegularListView(generic.ListView):
    model = GameTournamentRegular
    template_name = 'grizzly/pages/game-tournament-regular-list.html'

class GameTournamentRegularDetailView(generic.DetailView):
    model = GameTournamentRegular
    template_name = 'grizzly/pages/game-tournament-regular-detail.html'


class GameTournamentPlayOffListView(generic.ListView):
    model = GameTournamentPlayOff
    template_name = 'grizzly/pages/game-tournament-playoff-list.html'

class GameTournamentPlayOffDetailView(generic.DetailView):
    model = GameTournamentPlayOff
    template_name = 'grizzly/pages/game-tournament-playoff-detail.html'




class GameTournamentSystemListView(generic.ListView):
    model = GameTournamentSystem
    template_name = 'grizzly/pages/game-tournament-system-list.html'

class GameTournamentSystemDetailView(generic.DetailView):
    model = GameTournamentSystem
    template_name = 'grizzly/pages/game-tournament-system-detail.html'



class InsuranceTypeListView(generic.ListView):
    model = InsuranceType
    template_name = 'grizzly/pages/insurance-type-list.html'

class InsuranceTypeDetailView(generic.DetailView):
    model = InsuranceType
    template_name = 'grizzly/pages/insurance-type-detail.html'



class JudgeListView(generic.ListView):
    model = Judge
    template_name = 'grizzly/pages/judge-list.html'

class JudgeDetailView(generic.DetailView):
    model = Judge
    template_name = 'grizzly/pages/judge-detail.html'



class JudgeTypeListView(generic.ListView):
    model = JudgeType
    template_name = 'grizzly/pages/judge-type-list.html'

class JudgeTypeDetailView(generic.DetailView):
    model = JudgeType
    template_name = 'grizzly/pages/judge-type-detail.html'


class PlayerListView(generic.ListView):
    model = Player
    template_name = 'grizzly/pages/player-list.html'

class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'grizzly/pages/player-detail.html'

class TeamRequestView(generic.DetailView):
    model = Team
    template_name = 'grizzly/pages/team-request.html'
    
    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().order_by('player__role')


class PlayerStatusListView(generic.ListView):
    model = PlayerStatus
    template_name = 'grizzly/pages/player-status-list.html'

class PlayerStatusDetailView(generic.DetailView):
    model = PlayerStatus
    template_name = 'grizzly/pages/player-status-detail.html'



class PlayerTypeListView(generic.ListView):
    model = PlayerType
    template_name = 'grizzly/pages/player-type-list.html'

class PlayerTypeDetailView(generic.DetailView):
    model = PlayerType
    template_name = 'grizzly/pages/player-type-detail.html'



class RinkListView(generic.ListView):
    model = Rink
    template_name = 'grizzly/pages/rink-list.html'

class RinkDetailView(generic.DetailView):
    model = Rink
    template_name = 'grizzly/pages/rink-detail.html'



class RinkScheduleListView(generic.ListView):
    model = RinkSchedule
    template_name = 'grizzly/pages/rink-schedule-list.html'

class RinkScheduleDetailView(generic.DetailView):
    model = RinkSchedule
    template_name = 'grizzly/pages/rink-schedule-detail.html'



class TeamListView(generic.ListView):
    model = Team
    template_name = 'grizzly/pages/team-list.html'



class TeamDetailView(generic.DetailView):
    model = Team
    template_name = 'grizzly/pages/team-detail.html'



class TeamScheduleListView(generic.ListView):
    model = TeamSchedule
    template_name = 'grizzly/pages/team-schedule-list.html'

class TeamScheduleDetailView(generic.DetailView):
    model = TeamSchedule
    template_name = 'grizzly/pages/team-schedule-detail.html'



class TrainerListView(generic.ListView):
    model = Trainer
    template_name = 'grizzly/pages/trainer-list.html'

class TrainerDetailView(generic.DetailView):
    model = Trainer
    template_name = 'grizzly/pages/trainer-detail.html'



class TrainingListView(generic.ListView):
    model = Training
    template_name = 'grizzly/pages/training-list.html'

class TrainingDetailView(generic.DetailView):
    model = Training
    template_name = 'grizzly/pages/training-detail.html'




