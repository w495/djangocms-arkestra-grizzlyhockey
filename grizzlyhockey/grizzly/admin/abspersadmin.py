# -*- coding: utf-8 -*-

from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin


class AbsPersAdmin(PlaceholderAdmin):

    save_on_top = True

    list_display    = ('second_name', 'first_name', 'patronymic')
    list_filter     = tuple()
    search_fields   = ( 'second_name', 'first_name', 'patronymic')

    options_fieldsets = (
        ('параметры',{
            'fields': (
                'image',
                'second_name',
                'first_name',
                'patronymic',
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
