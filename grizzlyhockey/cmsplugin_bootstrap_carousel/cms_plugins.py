# coding: utf-8
import re
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_bootstrap_carousel.models import *
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.forms import ModelForm, ValidationError

import urllib2
import json 

class CarouselForm(ModelForm):
    class Meta:
        model = Carousel
    
    def clean_domid(self):
        data = self.cleaned_data['domid']
        if not re.match(r'^[a-zA-Z_]\w*$', data):
            raise ValidationError(_("The name must be a single word beginning with a letter"))
        return data

class CarouselItemInline(admin.StackedInline):
    model = CarouselItem

class CarouselPlugin(CMSPluginBase):
    model = Carousel
    form = CarouselForm
    name = _(u"Карусель картинок")
    render_template = "cmsplugin_bootstrap_carousel/carousel.html"

    inlines = [
        CarouselItemInline,
        ]

    def render(self, context, instance, placeholder):
        response = urllib2.urlopen('https://api.vk.com/method/photos.getAlbums?owner_id=-71330880&v=5.24')
        album_json = json.load(response)
        photo_size = 0
        my_instance = list()
        for album in album_json[u'response']['items']:
            if photo_size > 20:
                break
            album_title = album[u'title']
            album_id = album[u'id']
            response = urllib2.urlopen('https://api.vk.com/method/photos.get?owner_id=-71330880&v=5.24&album_id=' + str(album_id))
            photo_json = json.load(response)
            for photo in photo_json[u'response']['items']:
                if photo_size > 20:
                    break
                image_src = ""
                if not photo.has_key(u'width') or not photo.has_key(u'height') or (float(photo[u'width']) / float(photo[u'height']) < 1.3):
                    print float(photo[u'width']) / float(photo[u'height'])
                    continue
                
                if photo.has_key(u'photo_1280'):
                    image_src = photo[u'photo_1280']
                elif photo.has_key(u'photo_807'):
                    image_src = photo[u'photo_807']
                else:
                    continue
                photo_size += 1
                vk = CarouselItemVK(album_title, image_src)
                my_instance.append(vk)
        context.update({'instance' : instance, 'vk_instance' : my_instance})
        return context

plugin_pool.register_plugin(CarouselPlugin)
