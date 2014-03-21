# -*- coding: utf-8 -*-

from django.db import models
from absobj import AbsObj

class PlayerType(AbsObj):

    class Meta:
        app_label = "grizzly"
        verbose_name = "категорию игрока"
        verbose_name_plural = "игроки: категории игроков"
