# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class GameMatchGTime (AbsObj):


    gamematch = models.ForeignKey(
        'GameMatch',
        blank=True,
        null=True,
        verbose_name=u"Матч"
    )


    #alter table  grizzly_gamematchgtime add `minute` int(11) default null;
    #update grizzly_gamematchgtime set minute = minute(time) + hour(time) * 60;
    minute = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Минута"
    )

    #alter table  grizzly_gamematchgtime add `second` int(11) default null;
    #update grizzly_gamematchgtime set second = second(time);
    second = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Секунда"
    )

    #select g1.gamematch_id, g1.player_id, g1.minute, g1.second, g2.minute, g2.second  from grizzly_gamematchgtime as g1 join grizzly_gamematchgtime as g2 on g1.gamematch_id = g2.gamematch_id and g1.player_id = g2.player_id and g1.minute < g2.minute order by gamematch_id,  player_id;


    def get_time_points(self):
        res = None
        res =  [x for x in self.__class__.objects.raw(
            """
                select
                    g1.id,
                    g1.minute as start_minute,
                    g1.second as start_second,
                    g2.minute as stop_minute,
                    g2.second as stop_second
                from
                    grizzly_gamematchgtime as g1
                join
                    grizzly_gamematchgtime as g2
                on
                    g1.gamematch_id = g2.gamematch_id
                    and g1.player_id = g2.player_id
                    and g1.minute < g2.minute
                where
                    g1.id = %s or g2.id = %s
            """,
            [self.pk, self.pk]
        )]

        if(res):
            return res[0]

        obj = lambda:None
        obj.start_minute = None
        obj.stop_minute = None
        obj.start_second = None
        obj.stop_second = None

        return obj

    def get_start_minute(self):
        return self.get_time_points().start_minute


    def get_stop_minute(self):
        return self.get_time_points().stop_minute


    def get_start_second(self):
        return self.get_time_points().start_second


    def get_stop_second(self):
        return self.get_time_points().stop_second

    def get_diff_minute(self):

        if (None == self.stop_minute):
            return 0

        if (None == self.start_minute):
            return 0

        return abs(self.stop_minute - self.start_minute)


    def pre_save_action(self):
        obj = self.get_time_points()

        self.start_minute  = obj.start_minute
        self.stop_minute = obj.stop_minute
        self.start_second = obj.start_second
        self.stop_second = obj.stop_second


    #alter table  grizzly_gamematchgtime add `start_minute` int(11) default null;
    start_minute = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Минута начала"
    )

    #alter table  grizzly_gamematchgtime add `stop_minute` int(11) default null;
    stop_minute = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Минута конца"
    )

    #alter table  grizzly_gamematchgtime add `start_second` int(11) default null;
    start_second = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Секунда начала"
    )


    #alter table  grizzly_gamematchgtime add `stop_second` int(11) default null;
    stop_second = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = u"Секунда конца"
    )


    # alter table grizzly_gamematchgtime add team_id int(11) default null;
    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда",
    )

    # alter table grizzly_gamematchgtime add player_id int(11) default null;
    player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игрок"
    )

    a = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"А"
    )


    b = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"Б"
    )



    class Meta:
        ordering = ('ctime',)
        app_label = "grizzly"
        verbose_name = "Игра: матч: время игры вратарей"
        verbose_name_plural = "Игры: матчи: время игры вратарей"
