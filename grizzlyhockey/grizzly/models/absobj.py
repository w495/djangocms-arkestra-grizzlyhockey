# -*- coding: utf-8 -*-
import types

from django.db import models
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

from absabs import Absabs

class AbsObj(Absabs):
    '''
        Абстрактный объект
    '''

    name = models.CharField(
        max_length = 200,
        blank = True,
        null = True,
        verbose_name = u"название"
    )

    detail = models.TextField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"детали"
    )

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text = u"описание"
    )



    def __str__(self):
        return u"%s"%self.name

    def __unicode__(self):
        return u"%s"%self.name

    class Meta:
        ordering = ('name',)
        abstract = True
        app_label = "grizzly"

