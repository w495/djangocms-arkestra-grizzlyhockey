# -*- coding: utf-8 -*-

from django.db import models
from absschedule import AbsSchedule


class TeamSchedule(AbsSchedule):

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "команда: раcписание"
        verbose_name_plural = "команды: раcписания"
