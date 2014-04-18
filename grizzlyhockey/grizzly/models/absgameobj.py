# -*- coding: utf-8 -*-
import types

from django.db import models
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from absobj import AbsObj

class AbsGameObj(AbsObj):
    '''
        Абстрактный человек
    '''

    start_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u"дата начала"
    )

    stop_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u"дата конца"
    )



    def __str__(self):
        return u"%s"%self.name

    def __unicode__(self):
        return u"%s"%self.name

    class Meta:
        abstract = True
        app_label = "grizzly"
