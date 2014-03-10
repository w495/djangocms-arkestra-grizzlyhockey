
from south.db import db
from django.db import models
from semanticeditor.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'CssClass.templates'
        db.add_column('semanticeditor_cssclass', 'templates', orm['semanticeditor.cssclass:templates'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'CssClass.templates'
        db.delete_column('semanticeditor_cssclass', 'templates')
        
    
    
    models = {
        'semanticeditor.cssclass': {
            'allowed_elements': ('django.db.models.fields.CharField', [], {'default': "'h1 h2 h3 h4 h5 h6 p blockquote ul li row column'", 'max_length': '255'}),
            'column_equiv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'templates': ('semanticeditor.fields.MultiSelectField', ['"Templates"'], {'default': "''", 'blank': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        }
    }
    
    complete_apps = ['semanticeditor']
