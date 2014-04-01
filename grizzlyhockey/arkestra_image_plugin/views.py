from __future__ import division

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from easy_thumbnails.files import get_thumbnailer

from models import ImageSetItem

def lightbox_item(request, id=None, lightbox_max_dimension=400):     
    item = get_object_or_404(ImageSetItem, id=id)
    lightbox_max_dimension=int(lightbox_max_dimension)
    context = RequestContext(request)
    thumbnail_options = {} 

    # get width, height and lightbox_max_dimension
    lightbox_width, lightbox_height = item.image.width, item.image.height
    
    # get scaler value from width, height
    if max([lightbox_width, lightbox_height]) > lightbox_max_dimension:
        scaler = min(lightbox_max_dimension / dimension for dimension in [lightbox_width, lightbox_height]) 
        # set size of lightbox using scaler 
        item.width, item.height = lightbox_width * scaler, lightbox_height * scaler        
    else:
        item.width, item.height = lightbox_width, lightbox_height

    item.width, item.height = int(item.width), int(item.height)
                        
    thumbnail_options.update({
        'size': (item.width, item.height), 
        'subject_location': item.image.subject_location,
        })

    # get thumbnailer object for the image
    thumbnailer = get_thumbnailer(item.image)

    # apply options and get url
    item.large_url = thumbnailer.get_thumbnail(thumbnail_options).url  

    return render_to_response(
        "arkestra_image_plugin/lightbox_item.html",
        {
        "imageset_item":item,
        },
        RequestContext(request),
        )
