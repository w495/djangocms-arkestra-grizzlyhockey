# -*- coding: utf-8 -*-

from django.db import models
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

class AbsGameObj(models.Model):
    '''
        Абстрактный человек
    '''

    ctime = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u"дата создания",
    )

    image = FilerImageField(
        blank = True,
        null = True,
        verbose_name = u"картинка"
    )

    name = models.CharField(
        max_length = 200,
        verbose_name = u"название"
    )

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
        abstract = True
        app_label = "grizzly"
