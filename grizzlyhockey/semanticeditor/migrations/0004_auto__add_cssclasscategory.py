# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CssClassCategory'
        db.create_table('semanticeditor_cssclasscategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('semanticeditor', ['CssClassCategory'])


    def backwards(self, orm):
        
        # Deleting model 'CssClassCategory'
        db.delete_table('semanticeditor_cssclasscategory')


    models = {
        'semanticeditor.cssclass': {
            'Meta': {'ordering': "('verbose_name',)", 'object_name': 'CssClass'},
            'allowed_elements': ('django.db.models.fields.CharField', [], {'default': "'h1 h2 h3 h4 h5 h6 p blockquote ul ol li newrow newcol'", 'max_length': '255'}),
            'column_equiv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'templates': ('semanticeditor.fields.MultiSelectField', [], {'default': "''", 'blank': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'semanticeditor.cssclasscategory': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CssClassCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['semanticeditor']
