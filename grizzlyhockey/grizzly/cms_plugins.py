# -*- coding: utf-8 -*-

import operator
import datetime
import urllib2
import json 

from django.db.models import Q

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from grizzly.models import PlayerPlugin as PlayerPluginModel
from grizzly.models import TeamPlugin as TeamPluginModel
from grizzly.models import TeamPluginMany as TeamPluginManyModel

from grizzly.models import GameSeasonPlugin     as GameSeasonPluginModel
from grizzly.models import GameSeasonPluginMany as GameSeasonPluginManyModel

from grizzly.models import GameDivisionPlugin       as GameDivisionPluginModel
from grizzly.models import GameDivisionPluginMany   as GameDivisionPluginManyModel

from grizzly.models import GameTournamentRegularPlugin       as GameTournamentRegularPluginModel
from grizzly.models import GameTournamentRegularPluginMany   as GameTournamentRegularPluginManyModel

from grizzly.models import GameMatchPlugin      as GameMatchPluginModel
from grizzly.models import GameMatchPluginMany  as GameMatchPluginManyModel

from grizzly.models import GameMatch

from grizzly.models import Player

from grizzly.models import Banner
from grizzly.models import BannersPlugin as BannersPluginModel

from django.utils.translation import ugettext as _


class TeamPluginMany(CMSPluginBase):
    model = TeamPluginManyModel
    name = _(u"Гризли: несколько команд")
    render_template = "grizzly/plugins/teammany.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel  #
    name = _(u"Гризли: команда") #
    render_template = "grizzly/plugins/team.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



class PlayerPlugin(CMSPluginBase):
    model = PlayerPluginModel  #
    name = _(u"Гризли: игрок") #
    render_template = "grizzly/plugins/player.html" # template to render the plugin with
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameSeasonPlugin(CMSPluginBase):
    model = GameSeasonPluginModel  #
    name = _(u"Гризли: сезон") #
    render_template = "grizzly/plugins/gameseason.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameDivisionPlugin(CMSPluginBase):
    model = GameDivisionPluginModel  #
    name = _(u"Гризли: дивизион") #
    render_template = "grizzly/plugins/gamedivision.html"
    def render(self, context, instance, placeholder):
        division = instance.gamedivision
        query_set = division.get_queryset()
        
        max_ngoalsntrans_p2t = division.get_max_ngoalsntrans_p2t(query_set)
        max_ngoals_p2t = division.get_max_ngoals_p2t(query_set)
        max_ntrans_p2t = division.get_max_ntrans_p2t(query_set)
        min_nmisses_p2t = division.get_min_nmisses_p2t(query_set)
        
        context.update({ 'instance' : instance, 'max_ngoalsntrans_p2t' : max_ngoalsntrans_p2t,
                         'max_ngoals_p2t' : max_ngoals_p2t, 'max_ntrans_p2t' : max_ntrans_p2t,
                         'min_nmisses_p2t' : min_nmisses_p2t })
        return context

class GameDivisionPluginMany(CMSPluginBase):
    model = GameDivisionPluginManyModel  #
    name = _(u"Гризли: несколько дивизионов") #
    render_template = "grizzly/plugins/gamedivisionmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameTournamentRegularPlugin(CMSPluginBase):
    model = GameTournamentRegularPluginModel  #
    name = _(u"Гризли: регулярный чемпионат") #
    render_template = "grizzly/plugins/gametournamentregular.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameTournamentRegularPluginMany(CMSPluginBase):
    model = GameTournamentRegularPluginManyModel  #
    name = _(u"Гризли: несколько регулярных чемпионатов") #
    render_template = "grizzly/plugins/gametournamentregularmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class GameMatchPluginMany(CMSPluginBase):
    model = GameMatchPluginManyModel  #
    name = _(u"Гризли: несколько матчей") #
    render_template = "grizzly/plugins/gamematchmany.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameMatchPlugin(CMSPluginBase):
    model = GameMatchPluginModel  #
    name = _(u"Гризли: матч") #
    render_template = "grizzly/plugins/gamematch.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

class GameMatchSchedulePlugin(CMSPluginBase):
    name = _(u"Гризли: расписание матчей") #
    render_template = "grizzly/plugins/gamematchschedule.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

    def render(self, context, instance, placeholder):

        date = datetime.date.today()
        end_week = date + datetime.timedelta(10)
        gamematches =  GameMatch.objects.filter(
            start_datetime__range = [date, end_week]
        ).order_by('start_datetime')

        instance.gamematches = gamematches
        context['instance'] = instance
        return context


class PlayerBirthdayPlugin(CMSPluginBase):
    name = _(u"Гризли: Дни рождения") #
    render_template = "grizzly/plugins/playerbirthday.html"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

    def render(self, context, instance, placeholder):
        players =  self.birthdays_within()
        instance.players = players
        context['instance'] = instance
        return context

    def birthdays_within(self, days = 1):

        date = datetime.datetime.now()

        now = date - datetime.timedelta(days=0)
        then = date + datetime.timedelta(days=days)

        # Build the list of month/day tuples.
        monthdays = [(now.month, now.day)]
        while now <= then:
            monthdays.append((now.month, now.day))
            now += datetime.timedelta(days=1)

        # Tranform each into queryset keyword args.
        monthdays = (dict(zip(("birthday__month", "birthday__day"), t))
                    for t in monthdays)

        # Compose the djano.db.models.Q objects together for a single query.
        query = reduce(operator.or_, (Q(**d) for d in monthdays))

        # Run the query.

        players = [player for player in Player.objects.filter(query)]

        players = sorted(players, key = lambda x: x.birthday.month * 100 +  x.birthday.day)

        return players


class CarouselItemVK:
    caption_title = ""
    image_url = ""
    album_thumb_m = ""
    album_thumb_y = ""
    album_url = ""
    
    def __init__(self, title, url, thumb_tuple, album_url):
        self.caption_title = title
        self.image_url = url
        self.album_thumb_m = thumb_tuple[0]
        self.album_thumb_y = thumb_tuple[1]
        self.album_url = album_url
        

class VKPlugin(CMSPluginBase):
    name = _(u"VK фоточки")
    render_template = "grizzly/plugins/vk_carousel.html"

    def render(self, context, instance, placeholder):
        response = urllib2.urlopen('https://api.vk.com/method/photos.getAlbums?owner_id=-71330880&v=5.24&need_covers=1&photo_sizes=1')
        album_json = json.load(response)
        photo_size = 0
        my_instance = list()
        for album in album_json[u'response']['items']:
            if photo_size > 20:
                break
            album_title = album[u'title']
            album_id = album[u'id']
            album_thumb_m = ""
            album_thumb_y = ""
            album_url = "http://vk.com/grizzlyhockey?z=album-71330880_" + str(album_id)
            for size in album[u'sizes']:
                if size[u'type'] == 'm':
                    album_thumb_m = size[u'src']
                if size[u'type'] == 'y':
                    album_thumb_y = size[u'src']
            
            if album_thumb_y != "":
                vk = CarouselItemVK(album_title, album_thumb_y, (album_thumb_m, album_thumb_y), album_url)
                my_instance.append(vk)
            continue
            response = urllib2.urlopen('https://api.vk.com/method/photos.get?owner_id=-71330880&v=5.24&album_id=' + str(album_id))
            photo_json = json.load(response)
            for photo in photo_json[u'response']['items']:
                if photo_size > 20:
                    break
                image_src = ""
                if not photo.has_key(u'width') or not photo.has_key(u'height') or (float(photo[u'width']) / float(photo[u'height']) < 1.3):
                    continue
                
                if photo.has_key(u'photo_1280'):
                    image_src = photo[u'photo_1280']
                elif photo.has_key(u'photo_807'):
                    image_src = photo[u'photo_807']
                else:
                    continue
                photo_size += 1
                vk = CarouselItemVK(album_title, image_src, (album_thumb_m, album_thumb_y), album_url)
                my_instance.append(vk)
        context.update({'vk_instance' : my_instance})
        return context

class YoutubePlugin(CMSPluginBase):
    name = _(u"Youtube")
    render_template = "grizzly/plugins/youtube.html"

    def render(self, context, instance, placeholder):
        api_key = "AIzaSyAVwtnbo6GQY6-dIQmFXYwOBp3ZAwYDSyw"
        max_results = "10"
        playlist_id = "UUN21zKuol2253UKlXA_2UUg"
        #playlist_id = "UU55LbnVNxtcgZNkfeSui8YQ"
        response = urllib2.urlopen('https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=%s&playlistId=%s&fields=items&key=%s' % (max_results, playlist_id, api_key))
        youtube_json = json.load(response)
        #print youtube_json
        for item in youtube_json['items']:
            video_id = item['contentDetails']['videoId']
            video_url = "https://www.googleapis.com/youtube/v3/videos?id=%s&part=snippet&key=%s" % (video_id, api_key)
            #print video_url
        return context

class BannerPlugin(CMSPluginBase):
    model = BannersPluginModel  #
    name = _(u"Гризли: баннер") #
    render_template = "grizzly/plugins/banner.html"
    
    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(PlayerBirthdayPlugin)
plugin_pool.register_plugin(TeamPlugin)
plugin_pool.register_plugin(TeamPluginMany)
plugin_pool.register_plugin(PlayerPlugin)

plugin_pool.register_plugin(GameSeasonPlugin)

plugin_pool.register_plugin(GameDivisionPlugin)
plugin_pool.register_plugin(GameDivisionPluginMany)

plugin_pool.register_plugin(GameTournamentRegularPlugin)
plugin_pool.register_plugin(GameTournamentRegularPluginMany)

plugin_pool.register_plugin(GameMatchPlugin)

plugin_pool.register_plugin(GameMatchSchedulePlugin)

plugin_pool.register_plugin(GameMatchPluginMany)

plugin_pool.register_plugin(VKPlugin)
plugin_pool.register_plugin(YoutubePlugin)
plugin_pool.register_plugin(BannerPlugin)