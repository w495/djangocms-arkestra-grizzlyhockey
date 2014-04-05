# -*- coding: utf-8 -*-

from widgetry.tabs.placeholderadmin import ModelAdminWithTabsAndCMSPlaceholder
from cms.admin.placeholderadmin import PlaceholderAdmin

from autocomplete.widgets import *

from django.contrib.admin.options import ModelAdmin
from django.contrib.admin import widgets

class CustomModelAdmin:
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        """
        Get a form Field for a ManyToManyField.
        """
        # If it uses an intermediary model that isn't auto created, don't show
        # a field in admin.
        if not db_field.rel.through._meta.auto_created:
            return None
        db = kwargs.get('using')

        if db_field.name in self.raw_id_fields:
            kwargs['widget'] = widgets.ManyToManyRawIdWidget(db_field.rel, using=db)
            kwargs['help_text'] = ''
        else:
            kwargs['widget'] = widgets.FilteredSelectMultiple(db_field.verbose_name, False) # change second argument to True for filter_vertical

        return db_field.formfield(**kwargs)

ModelAdmin.__bases__ = (CustomModelAdmin,) + ModelAdmin.__bases__


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

