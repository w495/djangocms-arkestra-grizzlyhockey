# -*- coding: utf-8 -*-

from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin

from autocomplete.widgets import *

class AbsObjTabularInline(admin.TabularInline):
    related_search_fields = {}


class AbsObjAdmin(PlaceholderAdmin, AutocompleteModelAdmin):
    save_on_top = True
    readonly_fields  = (
        'id',
        'ctime'
    )

    ordering = (
        '-id',
    )

    related_search_fields = {}



    list_display = ('name',)
    list_filter = tuple()
    search_fields = ('name',)

    options_fieldsets = (
        ('параметры',{
            'fields': (
                'image',
                'name',
                'detail',
            ),
        }),
    )

    description_fieldsets = (
        ('',{
            'fields': (
                'description',
            ),
        }),
    )

    options_tab = ('параметры', {
        'fieldsets': options_fieldsets,
    })

    description_tab =  ('description', {
        'fieldsets': description_fieldsets,
    })

    tabs = (
        options_tab,
        description_tab
    )
