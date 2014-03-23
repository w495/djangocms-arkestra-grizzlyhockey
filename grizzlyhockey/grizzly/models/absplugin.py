# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin

from absobj import AbsObj

class AbsPlugin(CMSPlugin):
    '''
        Абстрактный объект
    '''
    ctime = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u"ctime"
    )

    name = models.CharField(
        max_length = 200,
        verbose_name = u"название"
    )

    class Meta:
        ordering = ('name',)
        abstract = True
        app_label = "grizzly"

