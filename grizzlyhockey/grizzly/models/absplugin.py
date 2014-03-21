# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin

from absobj import AbsObj

class AbsPlugin(CMSPlugin, AbsObj):
    '''
        Абстрактный объект
    '''

    class Meta:
        ordering = ('name',)
        abstract = True
        app_label = "grizzly"

