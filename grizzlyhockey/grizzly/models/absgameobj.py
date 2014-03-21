# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class AbsGameObj(AbsObj):
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

    class Meta:
        abstract = True
        app_label = "grizzly"
