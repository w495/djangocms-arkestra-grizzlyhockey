from django.conf.urls.defaults import patterns, url
from semanticeditor.views import *

urlpatterns = patterns('',
    url(r'retrieve_styles/', retrieve_styles, name="semantic.retrieve_styles"),
    url(r'retrieve_commands/', retrieve_commands, name="semantic.retrieve_commands"),
    url(r'separate_presentation/', separate_presentation, name="semantic.separate_presentation"),
    url(r'combine_presentation/', combine_presentation, name="semantic.combine_presentation"),
    url(r'clean_html/', clean_html_view, name="semantic.clean_html"),
    url(r'preview/', preview, name="semantic.preview"),
)
