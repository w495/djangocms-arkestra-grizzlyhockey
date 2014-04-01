# -*- coding: utf-8 -*-

from django.db import models
from absschedule import AbsSchedule
from rink import Rink

class RinkSchedule(AbsSchedule):

    rinks = models.ManyToManyField(
        'Rink',
        blank=True,
        null=True,
        through = Rink.rinkschedules.through,
        verbose_name=u"катки"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "каток: раcписание"
        verbose_name_plural = "катки: раcписания"
