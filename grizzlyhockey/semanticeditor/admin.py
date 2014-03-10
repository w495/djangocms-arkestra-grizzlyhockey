from django import forms
from django.contrib import admin
from semanticeditor.models import CssClass, CssClassCategory

class CssClassAdminInline(admin.StackedInline):
    model = CssClass
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'verbose_name'),
                ('description', 'templates',),
                ('allowed_elements', 'column_equiv'),
            ),
        }),
    )

class CssClassForm(forms.ModelForm):
    class Meta:
        model = CssClass
        widgets = {
            'templates': forms.SelectMultiple,
        }


class CssClassAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', 'name', 'category', 'allowed_elements')
    list_editable = ('name', 'category', 'allowed_elements')
    form = CssClassForm


class CssClassCategoryAdmin(admin.ModelAdmin):
    inlines = [CssClassAdminInline,]


admin.site.register(CssClass, CssClassAdmin)
admin.site.register(CssClassCategory, CssClassCategoryAdmin)
