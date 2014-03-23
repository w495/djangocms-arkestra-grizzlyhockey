# -*- coding: utf-8 -*-

from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin


class AbsObjAdmin(PlaceholderAdmin):
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
