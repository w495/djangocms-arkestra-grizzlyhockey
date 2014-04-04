from django.conf.urls import patterns, url

from grizzly import views

urlpatterns = patterns('',

    url(r'^player-type/$', views.PlayerTypeListView.as_view(), name='player-type-list'),

    url(r'^player-type/(?P<pk>\d+)/$', views.PlayerTypeDetailView.as_view(), name='player-type-detail'),


    url(r'^player/$', views.PlayerListView.as_view(), name='player-list'),

    url(r'^player/(?P<pk>\d+)/$', views.PlayerDetailView.as_view(), name='player-detail'),


    url(r'^judge-type/$', views.JudgeTypeListView.as_view(), name='judge-type-list'),

    url(r'^judge-type/(?P<pk>\d+)/$', views.JudgeTypeDetailView.as_view(), name='judge-type-detail'),


    url(r'^judge/$', views.JudgeListView.as_view(), name='judge-list'),

    url(r'^judge/(?P<pk>\d+)/$', views.JudgeDetailView.as_view(), name='judge-detail'),


    url(r'^trainer/$', views.TrainerListView.as_view(), name='trainer-list'),

    url(r'^trainer/(?P<pk>\d+)/$', views.TrainerDetailView.as_view(), name='trainer-detail'),


    url(r'^rink/$', views.RinkListView.as_view(), name='rink-list'),

    url(r'^rink/(?P<pk>\d+)/$', views.RinkDetailView.as_view(), name='rink-detail'),


    url(r'^team/$', views.TeamListView.as_view(), name='team-list'),

    url(r'^team/(?P<pk>\d+)/$', views.TeamDetailView.as_view(), name='team-detail'),


    url(r'^rink-schedule/$', views.RinkScheduleListView.as_view(), name='rink-schedule-list'),

    url(r'^rink-schedule/(?P<pk>\d+)/$', views.RinkScheduleDetailView.as_view(), name='rink-schedule-detail'),


    url(r'^team-schedule/$', views.TeamScheduleListView.as_view(), name='team-schedule-list'),

    url(r'^team-schedule/(?P<pk>\d+)/$', views.TeamScheduleDetailView.as_view(), name='team-schedule-detail'),



    url(r'^training/$', views.TrainingListView.as_view(), name='training-list'),

    url(r'^training/(?P<pk>\d+)/$', views.TrainingDetailView.as_view(), name='training-detail'),


    url(r'^game-season/$', views.GameSeasonListView.as_view(), name='game-season-list'),

    url(r'^game-season/(?P<pk>\d+)/$', views.GameSeasonDetailView.as_view(), name='game-season-detail'),



    url(r'^game-division/$', views.GameDivisionListView.as_view(), name='game-division-list'),

    url(r'^game-division/(?P<pk>\d+)/$', views.GameDivisionDetailView.as_view(), name='game-division-detail'),



    url(r'^game-tournament-regular/$', views.GameTournamentRegularListView.as_view(), name='game-tournament-regular-list'),

    url(r'^game-tournament-regular/(?P<pk>\d+)/$', views.GameTournamentRegularDetailView.as_view(), name='game-tournament-regular-detail'),


    url(r'^game-match/$', views.GameMatchListView.as_view(), name='game-match-list'),

    url(r'^game-match/(?P<pk>\d+)/$', views.GameMatchDetailView.as_view(), name='game-match-detail'),

    url(r'^game-match/schedule/$', views.GameMatchScheduleView.as_view(), name='game-match-schedule'),


    url(r'^game-match-goal/$', views.GameMatchGoalListView.as_view(), name='game-match-goal-list'),

    url(r'^game-match-goal/(?P<pk>\d+)/$', views.GameMatchGoalDetailView.as_view(), name='game-match-goal-detail'),



    url(r'^game-match-fine/$', views.GameMatchFineListView.as_view(), name='game-match-fine-list'),

    url(r'^game-match-fine/(?P<pk>\d+)/$', views.GameMatchFineDetailView.as_view(), name='game-match-fine-detail'),


    url(r'^game-match-gtime/$', views.GameMatchGTimeListView.as_view(), name='game-match-gtime-list'),

    url(r'^game-match-gtime/(?P<pk>\d+)/$', views.GameMatchGTimeDetailView.as_view(), name='game-match-gtime-detail'),


    url(r'^game-match-penalty/$', views.GameMatchPenaltyListView.as_view(), name='game-match-penalty-list'),

    url(r'^game-match-penalty/(?P<pk>\d+)/$', views.GameMatchPenaltyDetailView.as_view(), name='game-match-penalty-detail'),


    url(r'^insurance-type/$', views.InsuranceTypeListView.as_view(), name='insurance-type-list'),

    url(r'^insurance-type/(?P<pk>\d+)/$', views.InsuranceTypeDetailView.as_view(), name='insurance-type-detail'),


    url(r'^player-status/$', views.PlayerStatusListView.as_view(), name='player-status-list'),

    url(r'^player-status/(?P<pk>\d+)/$', views.PlayerStatusDetailView.as_view(), name='player-status-detail'),

)


