# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class AbsSchedule(AbsObj):
    '''
        Абстрактный человек
    '''

    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"дата начала"
    )

    stop_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"дата конца"
    )

    start_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время начала"
    )

    stop_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=u"время конца"
    )


    def __str__(self):
        return u"%s %s - %s %s"%(self.start_date, self.start_time, self.stop_date, self.stop_time)

    def __unicode__(self):
        return u"%s %s - %s %s"%(self.start_date, self.start_time, self.stop_date, self.stop_time)

    class Meta:
        abstract = True
        app_label = "grizzly"
