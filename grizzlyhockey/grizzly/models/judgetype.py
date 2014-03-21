# -*- coding: utf-8 -*-


from django.db import models
from absobj import AbsObj

class JudgeType(AbsObj):

    class Meta:
        app_label = "grizzly"
        verbose_name = "тип судейства"
        verbose_name_plural = "судьи: типы судейства"

