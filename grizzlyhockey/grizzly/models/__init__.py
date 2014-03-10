# -*- coding: utf-8 -*-

from django.db import models
import datetime
from django.utils import timezone
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from grizzly.pyadmin import verbose_name_cases, verbose_name_field_cases


class GrizzlyPlugin(CMSPlugin):
    player          = models.ForeignKey('Player',           related_name='plugins')
    judge           = models.ForeignKey('Judge',            related_name='plugins')
    judgetype       = models.ForeignKey('JudgeType',        related_name='plugins')
    playerstatus    = models.ForeignKey('PlayerStatus',     related_name='plugins')
    insurancetype   = models.ForeignKey('InsuranceType',    related_name='plugins')
    trainer         = models.ForeignKey('Trainer',          related_name='plugins')
    rink            = models.ForeignKey('Rink',             related_name='plugins')
    team            = models.ForeignKey('Team',             related_name='plugins')
    training        = models.ForeignKey('Training',         related_name='plugins')

    def __unicode__(self):
      return "GrizzlyPlugin"



class InsuranceType(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "тип страховки игрока"
        verbose_name_plural = "игроки: типы страховок"

class PlayerStatus(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "статус игрока"
        verbose_name_plural = "игроки: статусы игроков"


class PlayerType(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "категорию игрока"
        verbose_name_plural = "игроки: категории игроков"

class Player(models.Model):
    first_name  = models.CharField(max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")

    insurance_type = models.ForeignKey('InsuranceType', blank=True, null=True, verbose_name=u"тип страховки")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")

    height = models.IntegerField(verbose_name=u"рост");
    weight = models.IntegerField(verbose_name=u"вес");
    game_number = models.CharField(max_length=200, verbose_name=u"игровой номер")
    role          = models.CharField(max_length=200, verbose_name=u"амплуа")
    qualification = models.TextField(verbose_name=u"квалификация")

    status  = models.ForeignKey(PlayerStatus, blank=True, null=True, verbose_name=u"статус")
    type    = models.ForeignKey(PlayerType, blank=True, null=True, verbose_name=u"тип")

    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    class Meta:
        verbose_name        = "игрока"
        verbose_name_plural = "игроки"

class JudgeType(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "тип судейства"
        verbose_name_plural = "судьи: типы судейства"

class Judge(models.Model):
    first_name  = models.CharField(max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")
    types       = models.ManyToManyField(JudgeType, blank=True, null=True, verbose_name=u"что судит")

    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    class Meta:
        verbose_name        = "судьи"
        verbose_name_plural = "судьи"

class Trainer(models.Model):
    first_name  = models.CharField(max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")


    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)


    class Meta:
        verbose_name        = "тренера"
        verbose_name_plural = "тренеры"



class Rink(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")
    birthday    = models.DateTimeField(verbose_name=u"дата открытия")
    town        = models.CharField(max_length=200,verbose_name=u"город")
    street      = models.CharField(max_length=200,verbose_name=u"улица")
    house       = models.CharField(max_length=200,verbose_name=u"дом")
    building    = models.CharField(max_length=200,verbose_name=u"строение")


    def __unicode__(self):
        return self.name

    class Meta:
        ordering            = ('name',)
        verbose_name        = "каток"
        verbose_name_plural = "катки"


class Team(models.Model):
    name        = models.CharField(max_length=200, verbose_name=u"название")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")
    birthday    = models.DateField(auto_now_add=True, verbose_name=u"дата создания")
    players     = models.ManyToManyField(Player, verbose_name=u"Игроки")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name        = "команду"
        verbose_name_plural = "команды"

class Training(models.Model):
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    description = models.TextField(blank=True, null=True, verbose_name=u"описание")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    team    = models.ForeignKey('Team', blank=True, null=True, verbose_name=u"команда")
    rink    = models.ForeignKey('Rink', blank=True, null=True, verbose_name=u"каток")
    trainer = models.ForeignKey('Trainer', blank=True, null=True, verbose_name=u"тренер")

    date       = models.DateField(auto_now_add=True, verbose_name=u"дата")
    start_time = models.TimeField(auto_now_add=True, verbose_name=u"время начала")
    stop_time  = models.TimeField(auto_now_add=True, verbose_name=u"время конца")
    price      = models.IntegerField(verbose_name=u"Цена одного посещения")
    loan       = models.IntegerField(verbose_name=u"Абонемента")

    class Meta:
        ordering = ('date',)
        verbose_name        = "тренировку"
        verbose_name_plural = "тренировки"


