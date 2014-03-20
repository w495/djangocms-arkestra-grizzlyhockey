# -*- coding: utf-8 -*-

from django.db import models
import datetime
from django.utils import timezone
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from grizzly.pyadmin import verbose_name_cases, verbose_name_field_cases

from cms.models import Page, CMSPlugin
from cms.models.fields import PlaceholderField

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


    class Meta:
        verbose_name        = "тренировку"
        verbose_name_plural = "тренировки"


    def __unicode__(self):
      return u"Grizzly"




class InsuranceType(models.Model):
    name   = models.CharField(max_length=200, verbose_name=u"название")
    detail = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "тип страховки игрока"
        verbose_name_plural = "игроки: типы страховок"

class PlayerStatus(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name   = models.CharField(max_length=200, verbose_name=u"название")
    detail = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")


    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "статус игрока"
        verbose_name_plural = "игроки: статусы игроков"


class PlayerType(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name   = models.CharField(max_length=200, verbose_name=u"название")
    detail = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")


    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "категорию игрока"
        verbose_name_plural = "игроки: категории игроков"


class Player(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    first_name  = models.CharField(blank=True, null=True, max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(blank=True, null=True, max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(blank=True, null=True, max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(blank=True,null=True,verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")

    insurance_type = models.ForeignKey('InsuranceType', blank=True, null=True, verbose_name=u"тип страховки")

    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )

    height = models.IntegerField(blank=True, null=True, verbose_name=u"рост");
    weight = models.IntegerField(blank=True, null=True, verbose_name=u"вес");
    game_number = models.CharField(blank=True, null=True, max_length=200, verbose_name=u"игровой номер")
    role          = models.CharField(blank=True, null=True, max_length=200, verbose_name=u"амплуа")
    qualification = models.TextField(blank=True, null=True, verbose_name=u"квалификация")

    status  = models.ForeignKey(PlayerStatus, blank=True, null=True, verbose_name=u"статус")
    type    = models.ForeignKey(PlayerType, blank=True, null=True, verbose_name=u"тип")

    teams   = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    class Meta:
        verbose_name        = "игрока"
        verbose_name_plural = "игроки"

class PlayerPlugin(CMSPlugin):
    '''
        Плагин для отображения игрок в поле расширенного текста
    '''

    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    player      = models.ForeignKey(Player, verbose_name=u"игрок")
    class Meta:
        verbose_name        = "Гризли плагин: игрок"
        verbose_name_plural = "Гризли плагин: игрок"

    def __unicode__(self):
      return self.player



class JudgeType(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name        = models.CharField(max_length=200, verbose_name=u"название")
    detail = models.TextField(max_length=200, blank=True, null=True, verbose_name=u"детали")
    image       = FilerImageField(blank=True, null=True)

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "тип судейства"
        verbose_name_plural = "судьи: типы судейства"

class Judge(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    first_name  = models.CharField(max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(blank=True,null=True,verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    types       = models.ManyToManyField(
        'JudgeType',
        blank=True,
        null=True,
        verbose_name=u"что судит"
    )

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )


    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)

    class Meta:
        verbose_name        = "судьи"
        verbose_name_plural = "судьи"

class Trainer(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    first_name  = models.CharField(max_length=200, verbose_name=u"имя")
    patronymic  = models.CharField(max_length=200, verbose_name=u"отчество")
    second_name = models.CharField(max_length=200, verbose_name=u"фамилия")
    birthday    = models.DateField(blank=True,null=True,verbose_name=u"дата рождения")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"фотография")
    detail      = models.TextField(blank=True, null=True, verbose_name=u"детали")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )


    def __unicode__(self):
        return u"%s %s %s"%(self.second_name, self.first_name, self.patronymic)


    class Meta:
        verbose_name        = "тренера"
        verbose_name_plural = "тренеры"



class RinkSchedule(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail      = models.TextField(blank=True, null=True, verbose_name=u"детали")
    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )
    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")

    rinks   = models.ManyToManyField(
        'Rink',
        blank=True,
        null=True,
        verbose_name=u"катки"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering            = ('name',)
        verbose_name        = "каток: раcписание"
        verbose_name_plural = "катки: раcписания"


class Rink(models.Model):
    '''
        Каток
    '''
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name        = models.CharField(
        max_length=200,
        verbose_name=u"название"
    )

    ## Краткое описание простым текстом
    detail      = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"детали"
    )
    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',

        help_text="описание"
    )
    image       = FilerImageField(
        blank=True,
        null=True,
        verbose_name=u"картинка"
    )

    rinkschedules   = models.ManyToManyField(
        'RinkSchedule',
        blank=True,
        null=True,
        verbose_name=u"расписания"
    )

    birthday    = models.DateField(blank=True,null=True,verbose_name=u"дата открытия")
    town        = models.CharField(max_length=200,verbose_name=u"город")
    street      = models.CharField(max_length=200,verbose_name=u"улица")
    house       = models.CharField(max_length=200,verbose_name=u"дом")
    building    = models.CharField(max_length=200,verbose_name=u"строение")

    players     = models.ManyToManyField(Player, verbose_name=u"Игроки")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering            = ('name',)
        verbose_name        = "каток"
        verbose_name_plural = "катки"

class TeamSchedule(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail      = models.TextField(blank=True, null=True, verbose_name=u"детали")
    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )
    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")

    teams   = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering            = ('name',)
        verbose_name        = "команда: раcписание"
        verbose_name_plural = "команды: раcписания"


class Team(models.Model):
    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, verbose_name=u"название")
    detail      = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image       = FilerImageField(blank=True, null=True, verbose_name=u"картинка")
    birthday    = models.DateField(blank=True,null=True,verbose_name=u"дата создания")
    players     = models.ManyToManyField(
        'Player',
        blank=True,
        null=True,
        verbose_name=u"игроки"
    )

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    teamschedules   = models.ManyToManyField(
        'TeamSchedule',
        blank=True,
        null=True,
        verbose_name=u"расписания"
    )

    gamedivisions   = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name        = "команду"
        verbose_name_plural = "команды"


class TeamPlugin(CMSPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    team        = models.ForeignKey(Team, verbose_name=u"команда")
    class Meta:
        verbose_name        = "Гризли плагин: команда"
        verbose_name_plural = "Гризли плагин: команды"

    def __unicode__(self):
      return self.team


class TeamManyPlugin(CMSPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    teams       = models.ManyToManyField(
        Team,
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    class Meta:
        verbose_name        = "Гризли плагин: команды"
        verbose_name_plural = "Гризли плагин: команды"

    def __unicode__(self):
      return self.teams


class Training(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")

    name   = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    team    = models.ForeignKey('Team', blank=True, null=True, verbose_name=u"команда")
    rink    = models.ForeignKey('Rink', blank=True, null=True, verbose_name=u"каток")
    trainer = models.ForeignKey('Trainer', blank=True, null=True, verbose_name=u"тренер")

    date       = models.DateField(blank=True,null=True,verbose_name=u"дата")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")
    price      = models.IntegerField(verbose_name=u"Цена одного посещения")
    loan       = models.IntegerField(verbose_name=u"Абонемента")


    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering = ('date',)
        verbose_name        = "тренировку"
        verbose_name_plural = "тренировки"



class GameSeason (models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name   = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")
    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    gamedivisions   = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Игры: сезон"
        verbose_name_plural = "Игры: сезоны"

class GameSeasonPlugin(CMSPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''
    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    gameseason = models.ForeignKey(GameSeason, verbose_name=u"игровой сезон")
    def __unicode__(self):
      return self.name




class GameDivision(models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name   = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    gameseasons   = models.ManyToManyField(
        'GameSeason',
        blank=True,
        null=True,
        verbose_name=u"сезоны"
    )

    teams   = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering = ('ctime',)
        verbose_name        = "Игры: дивизион"
        verbose_name_plural = "Игры: дивизионы"

class GameDivisionManyPlugin(CMSPlugin):
    '''
        Плагин для отображения команды в поле расширенного текста
    '''

    ctime       = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name        = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    teams       = models.ManyToManyField(
        Team,
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )

    class Meta:
        verbose_name        = "Гризли плагин: дивизионы"
        verbose_name_plural = "Гризли плагин: дивизионы"

    def __unicode__(self):
      return self.teams


class GameDivisionPlugin(CMSPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''
    ctime        = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name         = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    gamedivision = models.ForeignKey(GameDivision, verbose_name=u"игровой дивизион")
    def __unicode__(self):
      return self.gamedivision




class GameTournamentFormat (models.Model):
    '''
        Формат соревнования: лига или кубок

        Под лигой мы принимаем круговой этап
            (круг --- все матчи сыгранные командами каждая с друг с другом)
            или регулярный чемпионат -
            это когда все заявленные команды помещаются
            в одну таблицу  (см. рис.1) и они играют с каждой командой
            один или несколько кругов.

        Кубок-это турнирная сетка плей-оф.
            Плей-оф может начинаться  с любого дробного значения
            (пример: 1/64, 1/32, 1/16, 1/8, 1/4, 1/2) кратное 2.

    '''
    ctime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u"ctime"
    )

    name = models.CharField(
        max_length=200,
        verbose_name=u"название"
    )
    detail = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"детали"
    )
    image  = FilerImageField(
        blank=True,
        null=True,
        verbose_name=u"картинка"
    )

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    class Meta:
        verbose_name        = "Игры: турниры: формат соревнования"
        verbose_name_plural = "Игры: турниры: форматы соревнования"



class GameTournamentSystem (models.Model):
    '''
        система соревнования:
            1. Регулярный чемпионат
            2. Регулярный чемпионат  + плей-оф
            3. Регулярный чемпионат + плей-оф+малый кубок-
                команды проигравшие на первой стадии плей-оф играют малый кубок
                в формате кубок или по круговой
            4. Регулярный чемпионат + плей-оф + кубок надежды
            5. Регулярный чемпионат+ плей-оф + малый кубок +кубок надежды
    '''
    ctime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u"ctime"
    )

    name = models.CharField(
        max_length=200,
        verbose_name=u"название"
    )
    detail = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=u"детали"
    )
    image  = FilerImageField(
        blank=True,
        null=True,
        verbose_name=u"картинка"
    )

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    class Meta:
        verbose_name        = "Игры: турниры: система соревнования"
        verbose_name_plural = "Игры: турниры: системы соревнования"


class GameTournament (models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name   = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )

    gamedivision    = models.ForeignKey('GameDivision', blank=True, null=True, verbose_name=u"дивизион")

    gametournamentformat = models.ForeignKey(
        'GameTournamentFormat',
        blank=True,
        null=True,
        verbose_name=u"формат соревнования"
    )

    gametournamentsystem = models.ForeignKey(
        'GameTournamentSystem',
        blank=True,
        null=True,
        verbose_name=u"система соревнования"
    )

    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering = ('ctime',)
        verbose_name        = "Игры: турнир"
        verbose_name_plural = "Игры: турниры"


class GameTournamentPlugin(CMSPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''
    ctime        = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name         = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    gametournament = models.ForeignKey(GameDivision, verbose_name=u"GameTournament")
    def __unicode__(self):
      return self.gametournament


class GameTournamentRegular (models.Model):
    ctime   = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name   = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"название")
    detail = models.TextField(blank=True, null=True, verbose_name=u"детали")
    image  = FilerImageField(blank=True, null=True, verbose_name=u"картинка")

    start_date = models.DateField(blank=True,null=True,verbose_name=u"дата начала")
    stop_date  = models.DateField(blank=True,null=True,verbose_name=u"дата конца")
    start_time = models.TimeField(blank=True,null=True,verbose_name=u"время начала")
    stop_time  = models.TimeField(blank=True,null=True,verbose_name=u"время конца")

    ## Подробное с возможностью вставлять расширенный текст.
    description = PlaceholderField(
        'body',
        help_text="описание"
    )


    gamedivisions = models.ManyToManyField(
        'GameDivision',
        blank=True,
        null=True,
        verbose_name=u"дивизионы"
    )


    teams = models.ManyToManyField(
        'Team',
        blank=True,
        null=True,
        verbose_name=u"команды"
    )


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        ordering = ('ctime',)
        verbose_name        = "Игры: турнир регулярный"
        verbose_name_plural = "Игры: турниры регулярные"


class GameTournamentRegularPlugin(CMSPlugin):
    '''
        Плагин для отображения в поле расширенного текста
    '''
    ctime        = models.DateTimeField(auto_now_add=True, verbose_name=u"ctime")
    name         = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"подпись")
    gametournamentregular = models.ForeignKey(GameDivision, verbose_name=u"GameTournamentRegular")
    def __unicode__(self):
      return self.gametournamentregular
