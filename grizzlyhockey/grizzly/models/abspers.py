# -*- coding: utf-8 -*-

from django.db import models
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

class AbsPers(models.Model):
    '''
        Абстрактный человек
    '''
    ctime = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u"ctime"
    )

    image = FilerImageField(
        blank = True,
        null = True,
        verbose_name = u"картинка"
    )

    first_name = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"имя"
    )

    patronymic = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"отчество"
    )

    second_name = models.CharField(
        blank = True,
        null = True,
        max_length = 200,
        verbose_name = u"фамилия"
    )

    birthday = models.DateField(
        blank = True,
        null = True,
        verbose_name = u"дата рождения"
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
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    class Meta:
        abstract = True
        app_label = "grizzly"
