# -*- coding: utf-8 -*-

from django.contrib import admin

from django.http import HttpResponseRedirect, HttpResponse


class AbsButtonableModelAdmin(admin.ModelAdmin):
    '''
        Миксин, добавляет новые действия (кнопки)
        к стандартным действиям админки.
        После выполнения действия переходит на предыдущую ссылку.
        В наследуемом классе должен быть определен атрибут
            buttons = [
                ('<action1>', <action1 description>)
                ('<action2>', <action2 description>)
                ...
            ]
        И соответствующие функции:
        def <action1>(self, request, obj):
            ...
        def <action2>(self, request, obj):
            ...
    '''

    def change_view(self, request, object_id, extra_context={}):
        extra_context['buttons'] = self.buttons
        return super(AbsButtonableModelAdmin, self).change_view(
                request=request, object_id=object_id, extra_context=extra_context)

    def button_view_dispatcher(self, request, object_id, command):
        obj = self.model._default_manager.get(pk=object_id)
        return getattr(self, command)(request, obj) \
                or HttpResponseRedirect(request.META['HTTP_REFERER'])

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url
        from django.utils.functional import update_wrapper
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        return patterns('',
            *(url(r'^(\d+)/(%s)/$' % but[0], wrap(self.button_view_dispatcher)) for but in self.buttons)
        ) + super(AbsButtonableModelAdmin, self).get_urls()


