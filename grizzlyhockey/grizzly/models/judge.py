# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers

class Judge(AbsPers):

    types = models.ManyToManyField(
        'JudgeType',
        blank=True,
        null=True,
        verbose_name=u"что судит"
    )

    class Meta:
        app_label = "grizzly"
        verbose_name = "судьи"
        verbose_name_plural = "судьи"

