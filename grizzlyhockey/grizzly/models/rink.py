# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class Rink (AbsObj):

    rinkschedules   = models.ManyToManyField(
        'RinkSchedule',
        blank=True,
        null=True,
        verbose_name=u"расписания"
    )

    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"дата открытия"
    )

    town = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"город"
    )

    street = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"улица"
    )

    house = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"дом"
    )

    building = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"строение"
    )

    class Meta:
        ordering            = ('name',)
        app_label           = "grizzly"
        verbose_name        = "каток"
        verbose_name_plural = "катки"
