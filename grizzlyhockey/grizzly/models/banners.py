# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

import logging

class Banner(AbsObj):
    # урл баннеры
    url = models.URLField(
        blank = True,
        null = True,
        verbose_name = u"урл",
        )
    
    # alter table grizzly_banner add `size` varchar(15) DEFAULT NULL;
    size = models.CharField(
        max_length = 15,
        blank = True,
        null = True,
        verbose_name = u"размер (в формате <ширина>x<высота>)"
    )
    
    # alter table grizzly_banner add `priority` int DEFAULT 0;
    priority = models.IntegerField(
        max_length = 15,
        blank = True,
        null = True,
        verbose_name = u"приоритет (чем выше тем лучше)"
    )

    class Meta:
        app_label = "grizzly"
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        
        
class BannerBlock(AbsObj):
    banners = models.ManyToManyField(
        'Banner',
        blank=True,
        null=True,
        verbose_name=u"баннеры",
        related_name="banners"
    )
    
    class Meta:
        app_label = "grizzly"
        verbose_name = "Блок баннера"
        verbose_name_plural = "Блок баннеров"
    
