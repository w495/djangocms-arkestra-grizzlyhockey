# -*- coding: utf-8 -*-

from django.db import models
from absplugin import AbsPlugin
from cms.models import CMSPlugin


class BannersPlugin(AbsPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''

    banners = models.ForeignKey(
        'BannerBlock',
        verbose_name=u"блок баннеров"
    )

    class Meta:
        ordering = ('name',)
        app_label = "grizzly"
        verbose_name = u"Гризли плагин: блок баннеров"
        verbose_name_plural = u"Гризли плагин: блок баннеров"

