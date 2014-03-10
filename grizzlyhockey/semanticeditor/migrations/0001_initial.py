
from south.db import db
from django.db import models
from semanticeditor.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'CssClass'
        db.create_table('semanticeditor_cssclass', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField("CSS class name", unique=True, max_length=255)),
            ('verbose_name', models.CharField("Human name", unique=True, max_length=255, blank=False)),
            ('description', models.TextField("Description", max_length=255, blank=True)),
            ('allowed_elements', models.CharField("Allowed HTML elements", default='h1 h2 h3 h4 h5 h6 p blockquote ul li row column', max_length=255)),
            ('column_equiv', models.IntegerField("Column count equivalent", null=True, blank=True)),
        ))
        db.send_create_signal('semanticeditor', ['CssClass'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'CssClass'
        db.delete_table('semanticeditor_cssclass')
        
    
    models = {
        'semanticeditor.cssclass': {
            'allowed_elements': ('django.db.models.fields.CharField', [], {'default': "'h1 h2 h3 h4 h5 h6 p blockquote ul li row column'", 'max_length': '255'}),
            'column_equiv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        }
    }

    complete_apps = ['semanticeditor']
