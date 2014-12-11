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
from playertype     import PlayerType

from player         import Player
#from player2team    import Player2Team
#from player2teamstat    import PlayerStat
#from player2teamstat    import Player2Stat
#from player2teamstat    import Player2TeamStat
from gameseason    import Player2Team
from gameseason    import PlayerStat
from gameseason    import Player2Stat


#from player2gamematcha    import Player2GameMatchA
#from player2gamematchb    import Player2GameMatchB

from playerplugin   import PlayerPlugin
from judgetype      import JudgeType
from judge          import Judge
from trainer        import Trainer
from rink           import Rink
#from team           import Team
from gameseason    import Team
from gameseason    import TeamStat
from gameseason    import TeamStatEntry
from gameseason    import Team2Stat

from finaltype      import FinalType

from rinkschedule   import RinkSchedule
from teamschedule   import TeamSchedule
from teamplugin     import TeamPlugin
from teampluginmany import TeamPluginMany
from training       import Training

from gameseason             import GameSeason
from gameseasonplugin       import GameSeasonPlugin
from gameseasonpluginmany   import GameSeasonPluginMany

from gamedivision           import GameDivision
from gamedivisionplugin     import GameDivisionPlugin
from gamedivisionpluginmany import GameDivisionPluginMany

from gametournamentformat   import GameTournamentFormat
from gametournamentsystem   import GameTournamentSystem


from gametournamentplayoff              import GameTournamentPlayOff
from gametournamentregular              import GameTournamentRegular
from gametournamentregularplugin        import GameTournamentRegularPlugin
from gametournamentregularpluginmany    import GameTournamentRegularPluginMany

from gamematch              import GameMatch
from gamematchplugin        import GameMatchPlugin
from gamematchpluginmany    import GameMatchPluginMany



from gamematchgoal          import GameMatchGoal
from gamefinetype           import GameFineType
from gamematchfine          import GameMatchFine
from gamematchgtime         import GameMatchGTime
from gamematchpenalty       import GameMatchPenalty

from banners import Banner
from banners import BannerBlock
from bannersplugin import BannersPlugin

from gametournamentregularplugin import GameTournamentRegularPlugin

