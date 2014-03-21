# -*- coding: utf-8 -*-

from django.db import models


from absobj import AbsObj
from abspers import AbsPers
from absschedule import AbsSchedule
from absgameobj import AbsGameObj
from absplugin import AbsPlugin


##
## Тип страховки игрока.
##
from insurancetype import InsuranceType

##
## Статус игрока
##
from playerstatus import PlayerStatus

##
## Категория игрока
##
from playertype import PlayerType

from player import Player
from playerplugin import PlayerPlugin
from judgetype import JudgeType
from judge import Judge
from trainer import Trainer
from rink import Rink
from team import Team

from rinkschedule   import RinkSchedule
from teamschedule   import TeamSchedule
from teamplugin     import TeamPlugin
from teampluginmany import TeamPluginMany
from training       import Training

from gameseason             import GameSeason
from gameseasonplugin       import GameSeasonPlugin
from gamedivision           import GameDivision
from gamedivisionplugin     import GameDivisionPlugin

from gamedivisionpluginmany import GameDivisionPluginMany

from gametournamentformat import GameTournamentFormat

from gametournamentsystem import GameTournamentSystem

from gametournamentregular import GameTournamentRegular

from gametournamentregularplugin import GameTournamentRegularPlugin

