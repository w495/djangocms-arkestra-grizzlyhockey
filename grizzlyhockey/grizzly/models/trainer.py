# -*- coding: utf-8 -*-

from django.db import models
from abspers import AbsPers

class Trainer(AbsPers):

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = "тренера"
        verbose_name_plural = "тренеры"


