from django.forms.models import ModelForm
from cms.plugins.text.models import Text
from django import forms
from semanticeditor.widgets import SemanticEditor

class SemanticTextForm(ModelForm):
    body = forms.CharField(widget=SemanticEditor())
    class Meta:
        model = Text
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
