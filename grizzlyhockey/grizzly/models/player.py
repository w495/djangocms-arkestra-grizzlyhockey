# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers
from gamematchgoal import GameMatchGoal
from django.db.models import Q

class Player(AbsPers):

    insurance_type = models.ForeignKey(
        'InsuranceType',
        blank = True,
        null = True,
        verbose_name = u"тип страховки"
    )

    height = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"рост"
    )

    weight = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"вес"
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

    qualification = models.TextField(
        blank = True,
        null = True,
        verbose_name = u"квалификация"
    )

    status = models.ForeignKey(
        'PlayerStatus',
        blank = True,
        null = True,
        verbose_name = u"статус"
    )

    type = models.ForeignKey(
        'PlayerType',
        blank = True,
        null = True,
        verbose_name = u"тип"
    )

    teams = models.ManyToManyField(
        'Team',
        blank = True,
        null = True,
        through='Player2Team',
        verbose_name = u"команды"
    )
    
    gamematchgoal_trans = models.ManyToManyField(
        'GameMatchGoal',
        blank=True,
        null=True,
        through=GameMatchGoal.trans_players.through,
        verbose_name=u"игроки, сделавшие результативную передачу"
    )
    
    # alter table grizzly_playerstat add rating double precision default 0.0;
    rating = models.FloatField(
        verbose_name=u"Рейтинг",
        blank=True,
        null=True,
        default=0.0
    )
    
    def post_save(self):
        self.update_rating()
    
    def resave_player2team_set(self):
        [p2t.async_resave() for p2t in self.player2team_set.all()]
    
    def get_nwingames(self):
        ngames = 0
        ngames += self.gamematch_a.filter( Q(score_a__gt = models.F('score_b')) ).distinct().count()
        ngames += self.gamematch_b.filter( Q(score_b__gt = models.F('score_a')) ).distinct().count()
        return ngames
    
    def get_nlosegames(self):
        ngames = 0
        ngames += self.gamematch_a.filter( Q(score_b__gt = models.F('score_a')) ).distinct().count()
        ngames += self.gamematch_b.filter( Q(score_a__gt = models.F('score_b')) ).distinct().count()
        return ngames
    
    def get_ndrawsgames(self):
        ngames = 0
        ngames += self.gamematch_a.filter( Q(score_a = models.F('score_b')) ).distinct().count()
        ngames += self.gamematch_b.filter( Q(score_b = models.F('score_a')) ).distinct().count()
        return ngames
    
    def get_ngoals(self, is_power_play, is_short_handed):
        return len(self.gamematchgoal_goal.filter(is_power_play = is_power_play, is_short_handed = is_short_handed))
    
    def get_win_goals(self):
        return len(self.gamematchgoal_goal.filter(is_win_goal = 1))
    
    def get_ntrans(self, is_power_play, is_short_handed):
        return len(self.gamematchgoal_assistant_1.filter(is_power_play = is_power_play, is_short_handed = is_short_handed)) + len(self.gamematchgoal_assistant_2.filter(is_power_play = is_power_play, is_short_handed = is_short_handed))
    
    def update_rating(self):
        """(!) Игрок забил гол    0,5
           (!) Игрок отдал пас 0,3
           (!) Игрок забил в большинстве    0,25
           (!) Игрок отдал пас в большинстве   0,15
           (!) Победная шайба  0,1
           (!) Игрок забил гол в меньшинстве   0,75
           (!) Игрок отдал пас в меньшинстве   0,4
           (!) Победа команды (каждому игроку) 0,5
           (!) Игра в ничью (каждому игроку)   0,25
           (!) Игрок находящийся во время гола на площадке 0,2
           (!) Пропущенная шайба при равенстве команд: -0,3 всем игрокам, находившимся на площадке
           (!) Пропущенная шайба в меньшинстве: -0,15 всем игрокам, находившимся на площадке
           (!) Пропущенная шайба в большинстве: -0,5 всем игрокам, находившимся на площадке
           (!) Проигрыш команды (каждому игроку)   -0,3
           (!) Удаление 2 мин  -0,1
           (!) Удаление 4 мин  -0,15
           (!) Удаление 2 мин+10   -0,2
           (!) Удаление 4 мин+10   -0,25
           (!) Удаление 5 мин +10  -0,3
           (!) Удаление  5+20  -0,35
           (!) Удаление 25 мин -0,4"""
        
        fines_map = dict()
        fines = 0
        for fine in self.gamematchfine_set.all():
            fines += fine.minutes
            if fines_map.has_key(fine.minutes):
                fines_map[fine.minutes] += 1
            else:
                fines_map[fine.minutes] = 1
        
        ntrans = self.get_ntrans(0, 0)
        ngoals = self.get_ngoals(0, 0)
        
        ntrans_power_play = self.get_ntrans(1, 0)
        ngoals_power_play = self.get_ngoals(1, 0)
        
        ntrans_short_handed = self.get_ntrans(0, 1)
        ngoals_short_handed = self.get_ngoals(0, 1)
        
        nwinsgames = self.get_nwingames()
        nlosegames = self.get_nlosegames()
        ndrawsgames = self.get_ndrawsgames()
        
        #goal_in_rink = len(self.gamematchgoal_rink_players_a.all()) + len(self.gamematchgoal_rink_players_b.all())
        
        goal_games = 0
        lose_games = 0
        lose_games_power_play = 0
        lose_games_short_handed = 0
        for goal in self.gamematchgoal_rink_players_a.all():
            team = goal.team
            team_winner = False
            team_loser = False
            for player_a in goal.rink_players_a.all():
                if player_a.player == self:
                    if player.team == team:
                        team_winner = True
                    else:
                        team_loser = True
                    break
            if team_loser:
                if goal.is_power_play:
                    lose_games_short_handed += 1
                elif goal.is_short_handed:
                    lose_games_power_play += 1
                else:
                    lose_games += 1
            elif team_winner:
                goal_games += 1
        
        for goal in self.gamematchgoal_rink_players_b.all():
            team = goal.team
            team_winner = False
            team_loser = False
            for player_b in goal.rink_players_b.all():
                if player_b.player == self:
                    if player.team == team:
                        team_winner = True
                    else:
                        team_loser = True
                    break
            if team_loser:
                if goal.is_power_play:
                    lose_games_short_handed += 1
                elif goal.is_short_handed:
                    lose_games_power_play += 1
                else:
                    lose_games += 1
            elif team_winner:
                goal_games += 1
        
        nwingoal = self.get_win_goals()
        
        self.rating = 0.5 * ngoals + 0.3 * ntrans + 0.25 * ngoals_power_play + 0.15 * ntrans_power_play + \
                      0.1 * nwingoal + 0.75 * ngoals_short_handed + 0.4 * ntrans_short_handed + 0.5 * nwinsgames + \
                      + 0.25 * ndrawsgames - 0.3 * nlosegames + \
                      + 0.2 * goal_games - 0.3 * lose_games - 0.15 * lose_games_short_handed - 0.5 * lose_games_power_play + \
                      -0.1 * fines_map.get(2, 0) - 0.15 * fines_map.get(4, 0) - 0.2 * fines_map.get(12, 0) + \
                      -0.25 * fines_map.get(14, 0) - 0.3 * fines_map.get(15, 0) - 0.35 * fines_map.get(25, 0) 
        self.save()
    
    def __str__(self):
        return u"%s, %s %s %s"%(self.game_number, self.second_name, self.first_name, self.patronymic)

    def __unicode__(self):
        return u"%s, %s %s %s"%(self.game_number, self.second_name, self.first_name, self.patronymic)


    class Meta:
        app_label = "grizzly"
        verbose_name = "игрока"
        verbose_name_plural = "игроки"
