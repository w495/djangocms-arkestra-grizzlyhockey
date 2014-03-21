# -*- coding: utf-8 -*-

from django.db import models
from absschedule import AbsSchedule



class Training(AbsSchedule):

    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команда"
    )

    rink = models.ForeignKey(
        'Rink',
        blank=True,
        null=True,
        verbose_name=u"каток"
    )

    trainer = models.ForeignKey(
        'Trainer',
        blank=True,
        null=True,
        verbose_name=u"тренер"
    )

    price = models.IntegerField(
        verbose_name=u"Цена одного посещения"
    )

    loan = models.IntegerField(
        verbose_name=u"Цена абонемента"
    )

    class Meta:
        ordering = ('start_date',)
        app_label = "grizzly"
        verbose_name = "тренировку"
        verbose_name_plural = "тренировки"
