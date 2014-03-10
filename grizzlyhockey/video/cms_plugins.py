import os, models, bisect

from threading import Thread

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from arkestra_utilities.output_libraries.plugin_widths import *
from arkestra_utilities.settings import USE_CELERY_FOR_VIDEO_ENCODING

from models import VideoPluginEditor, VideoVersion, CODECS, VERSIONS, SIZES, PLAYERS

if USE_CELERY_FOR_VIDEO_ENCODING:
    from tasks import encodevideo

class VideoPluginPublisher(CMSPluginBase):
    model = VideoPluginEditor
    name = _("Video")
    render_template = "video/video.html"
    text_enabled = True
    admin_preview = False
    raw_id_fields = ('video',)
            
    def icon_src(self, instance):
        return "/static/plugin_icons/video.png"

    def render(self, context, instance, placeholder):
        """
        Arkestra can calculate the exact pixel width of any column in any placeholder; however, this isn't available to all applications that might use the filer.
        
        So, we should make the calculations here optional, and for non-Arkestra implementations do something different
        """        
        print "****"
        instance.has_borders = False
         
        # calculate the width of the placeholder
        placeholder_width = get_placeholder_width(context, instance)

        # widths a fraction of nominal container width (deprecated)
        if instance.width <= 10:
         width = placeholder_width/instance.width
 
        # widths relative to placeholder width
        else:
         # widths a percentage of placeholder width
         if instance.width <= 100:
             width = placeholder_width/100.0 * instance.width
             auto = False

         # automatic width      
         elif instance.width == 1000:
             width = placeholder_width
             auto = True
 
         # calculate the width of the block the image will be in
         width = calculate_container_width(context, instance, width, auto)
        
        # shave off 5 point if the image is floated, to make room for a margin
        # see arkestra.css, span.image.left and span.image.right
        if instance.float:
         width = width - 5   

        if instance.use_description_as_caption:
         instance.caption = instance.caption or instance.video.description

        # given the width we want to show the video at, we have to find the most suitable (i.e. closest larger) video file version we have created
        index = bisect.bisect_left(SIZES,width)
        if index < len(SIZES): # not larger than the largest preset size?
         size = SIZES[index] # get the exact or closest larger size
        else:
         # choose the widest, if we don't have one wider
         size = SIZES[-1]

        # create the lists of missing and available items
        instance.ready_versions = []
        instance.unready_versions = []

        for codec, codec_dictionary in CODECS.items():
         version, created = VideoVersion.objects.get_or_create(source = instance.video, size = size, codec = codec)

         # get the version's codec_and_size identifier string
         codec_and_size = version.codec_and_size()
             
         # get the file path for the version
         videofilepath = version.outputpath()

         # does the file exist?
         print "**"
         print "** version", codec_and_size
         print "** version status", version.status
         if os.path.exists(videofilepath): 
             print "** file exists", videofilepath
             # if it does, check that the status dictionary agrees
             if version.status == "ready":
                 print "** version is ready"

                 # and add the version to available_versions
                 instance.ready_versions.append(codec)
             else:
                 # what if the status dictionary doesn't say that the file is ready?
                 print "** version is not ready"
                 instance.unready_versions.append(codec)

                 # unless status check says it's encoding, it must be "missing" or "failed"- so let's try to encode it
                 if version.status != "encoding":

                     if USE_CELERY_FOR_VIDEO_ENCODING:
                         print "** launching encodevideo()"
                         version_status = encodevideo.delay(source = instance.video, size = size, codec = codec)
                         print "** got back from encodevideo()", version_status
                     else:
                         thread = Thread(target=version.encode, name=videofilepath)
                         thread.start()

         # if the file doesn't exist
         else:
             print "** file doesn't exist", videofilepath
             version.status = "missing"
             instance.unready_versions.append(codec)

             if USE_CELERY_FOR_VIDEO_ENCODING:
                 encodevideo.delay(source = instance.video, size = size, codec = codec)
                 print "** launching encodevideo() for", codec_and_size
             else:
                 thread = Thread(target=version.encode, name=videofilepath)
                 thread.start()

        # now we need to list the formats available to the different players (HTML5 and Flash so far, 
        # but we could have others if we wanted). The same format (H.264) is currently used for both 
        # HTML5 and Flash

        instance.html5_formats = []
        instance.flash_formats = []
        # all_formats is a list of versions without any duplications
        instance.all_formats = []
        instance.ready_versions = set(instance.ready_versions)

        # let's assemble the list of versions available for the HTML5 player
        # instance.formats is a dict of players, containing the appropriate codec dicts from ready_versions
        instance.formats = {}
        for player, player_codecs in PLAYERS.items():
         instance.formats[player] = []
         for codec in player_codecs:
             if codec in instance.ready_versions:
                 # add all the information we'll need about this version to a dictionary
                 description = {"url": VideoVersion.objects.get(source = instance.video, codec = codec, size = size).url(), "type": VERSIONS[codec][size]["type"], "description": CODECS[codec]["description"], "implications": CODECS[codec]["implications"],}
                 instance.formats[player].append(description)
                 if description not in instance.all_formats:
                     instance.all_formats.append(description)

        instance.width = int(width)
        instance.dumb_height = int(instance.width * .75)
        instance.size = size
        context.update({
            'video':instance,
            # 'width': int(width),
            # 'caption_width': int(width),
            'placeholder':placeholder,
        })
        return context

plugin_pool.register_plugin(VideoPluginPublisher)
