# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GrizzlyPlugin'
        db.create_table('cmsplugin_grizzlyplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Player'])),
            ('judge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Judge'])),
            ('judgetype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.JudgeType'])),
            ('playerstatus', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.PlayerStatus'])),
            ('insurancetype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.InsuranceType'])),
            ('trainer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Trainer'])),
            ('rink', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Rink'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Team'])),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['grizzly.Training'])),
        ))
        db.send_create_signal('grizzly', ['GrizzlyPlugin'])

        # Adding model 'InsuranceType'
        db.create_table('grizzly_insurancetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['InsuranceType'])

        # Adding model 'PlayerStatus'
        db.create_table('grizzly_playerstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('in_lists', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('body', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('hosted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='playerstatus_hosted_events', on_delete=models.SET_DEFAULT, default=1, to=orm['contacts_and_people.Entity'], blank=True, null=True)),
            ('importance', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['PlayerStatus'])

        # Adding M2M table for field publish_to on 'PlayerStatus'
        m2m_table_name = db.shorten_name('grizzly_playerstatus_publish_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playerstatus', models.ForeignKey(orm['grizzly.playerstatus'], null=False)),
            ('entity', models.ForeignKey(orm['contacts_and_people.entity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['playerstatus_id', 'entity_id'])

        # Adding M2M table for field please_contact on 'PlayerStatus'
        m2m_table_name = db.shorten_name('grizzly_playerstatus_please_contact')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playerstatus', models.ForeignKey(orm['grizzly.playerstatus'], null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['playerstatus_id', 'person_id'])

        # Adding model 'PlayerType'
        db.create_table('grizzly_playertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['PlayerType'])

        # Adding model 'Player'
        db.create_table('grizzly_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('insurance_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.InsuranceType'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('game_number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('qualification', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.PlayerStatus'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.PlayerType'], null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['Player'])

        # Adding model 'JudgeType'
        db.create_table('grizzly_judgetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['JudgeType'])

        # Adding model 'Judge'
        db.create_table('grizzly_judge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['Judge'])

        # Adding M2M table for field types on 'Judge'
        m2m_table_name = db.shorten_name('grizzly_judge_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('judge', models.ForeignKey(orm['grizzly.judge'], null=False)),
            ('judgetype', models.ForeignKey(orm['grizzly.judgetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['judge_id', 'judgetype_id'])

        # Adding model 'Trainer'
        db.create_table('grizzly_trainer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['Trainer'])

        # Adding model 'Rink'
        db.create_table('grizzly_rink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')()),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('grizzly', ['Rink'])

        # Adding model 'Team'
        db.create_table('grizzly_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('grizzly', ['Team'])

        # Adding M2M table for field players on 'Team'
        m2m_table_name = db.shorten_name('grizzly_team_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['grizzly.team'], null=False)),
            ('player', models.ForeignKey(orm['grizzly.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'player_id'])

        # Adding model 'Training'
        db.create_table('grizzly_training', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.Team'], null=True, blank=True)),
            ('rink', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.Rink'], null=True, blank=True)),
            ('trainer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grizzly.Trainer'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('stop_time', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('loan', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('grizzly', ['Training'])


    def backwards(self, orm):
        # Deleting model 'GrizzlyPlugin'
        db.delete_table('cmsplugin_grizzlyplugin')

        # Deleting model 'InsuranceType'
        db.delete_table('grizzly_insurancetype')

        # Deleting model 'PlayerStatus'
        db.delete_table('grizzly_playerstatus')

        # Removing M2M table for field publish_to on 'PlayerStatus'
        db.delete_table(db.shorten_name('grizzly_playerstatus_publish_to'))

        # Removing M2M table for field please_contact on 'PlayerStatus'
        db.delete_table(db.shorten_name('grizzly_playerstatus_please_contact'))

        # Deleting model 'PlayerType'
        db.delete_table('grizzly_playertype')

        # Deleting model 'Player'
        db.delete_table('grizzly_player')

        # Deleting model 'JudgeType'
        db.delete_table('grizzly_judgetype')

        # Deleting model 'Judge'
        db.delete_table('grizzly_judge')

        # Removing M2M table for field types on 'Judge'
        db.delete_table(db.shorten_name('grizzly_judge_types'))

        # Deleting model 'Trainer'
        db.delete_table('grizzly_trainer')

        # Deleting model 'Rink'
        db.delete_table('grizzly_rink')

        # Deleting model 'Team'
        db.delete_table('grizzly_team')

        # Removing M2M table for field players on 'Team'
        db.delete_table(db.shorten_name('grizzly_team_players'))

        # Deleting model 'Training'
        db.delete_table('grizzly_training')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 20, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('site', 'tree_id', 'lft')", 'object_name': 'Page'},
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contacts_and_people.building': {
            'Meta': {'ordering': "('site', 'street', 'number', 'name')", 'object_name': 'Building'},
            'access_and_parking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'building_access_and_parking'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'additional_street_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'building_description'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'getting_here': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'getting_here'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'map': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'place'", 'on_delete': 'models.PROTECT', 'to': "orm['contacts_and_people.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {'default': '17', 'null': 'True', 'blank': 'True'})
        },
        'contacts_and_people.entity': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Entity', '_ormbases': ['contacts_and_people.EntityLite']},
            'abstract_entity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'access_note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'auto_contacts_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_news_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_vacancies_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Building']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'building_recapitulates_entity_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contacts_page_intro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts_page_intro'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'contacts_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'Contacts & people'", 'max_length': '50'}),
            'display_parent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'entitylite_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts_and_people.EntityLite']", 'unique': 'True', 'primary_key': 'True'}),
            'external_url': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'entity_item'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['links.ExternalLink']"}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'news_page_intro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'news_page_intro'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'news_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'News & events'", 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['contacts_and_people.Entity']"}),
            'precise_location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vacancies_page_intro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vacancies_page_intro'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'vacancies_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'Vacancies & studentships'", 'max_length': '50'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cms.Page']", 'blank': 'True', 'unique': 'True'})
        },
        'contacts_and_people.entitylite': {
            'Meta': {'object_name': 'EntityLite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contacts_and_people.membership': {
            'Meta': {'ordering': "('-importance_to_entity', 'person__surname')", 'object_name': 'Membership'},
            'display_role': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'display_roles'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['contacts_and_people.Membership']"}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': "orm['contacts_and_people.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance_to_entity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'importance_to_person': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'key_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_of'", 'to': "orm['contacts_and_people.Person']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'contacts_and_people.person': {
            'Meta': {'ordering': "['surname', 'given_name', 'user']", 'object_name': 'Person', '_ormbases': ['contacts_and_people.PersonLite']},
            'access_note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Building']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'data_feed_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'entities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'people'", 'to': "orm['contacts_and_people.Entity']", 'through': "orm['contacts_and_people.Membership']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'external_url': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_item'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['links.ExternalLink']"}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'institutional_username': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'override_entity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_override'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['contacts_and_people.Entity']"}),
            'personlite_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts_and_people.PersonLite']", 'unique': 'True', 'primary_key': 'True'}),
            'please_contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_for'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['contacts_and_people.Person']"}),
            'precise_location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60', 'blank': 'True'}),
            'staff_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_user'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']", 'blank': 'True', 'unique': 'True'})
        },
        'contacts_and_people.personlite': {
            'Meta': {'object_name': 'PersonLite'},
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Title']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'contacts_and_people.phonecontact': {
            'Meta': {'ordering': "('label',)", 'object_name': 'PhoneContact'},
            'area_code': ('django.db.models.fields.CharField', [], {'default': "'029'", 'max_length': '5'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'default': "'44'", 'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_extension': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'contacts_and_people.site': {
            'Meta': {'ordering': "('country', 'site_name', 'post_town')", 'object_name': 'Site'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_town': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'contacts_and_people.title': {
            'Meta': {'ordering': "['title']", 'object_name': 'Title'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'grizzly.grizzlyplugin': {
            'Meta': {'object_name': 'GrizzlyPlugin', 'db_table': "'cmsplugin_grizzlyplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'insurancetype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.InsuranceType']"}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Judge']"}),
            'judgetype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.JudgeType']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Player']"}),
            'playerstatus': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.PlayerStatus']"}),
            'rink': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Rink']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Team']"}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Trainer']"}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['grizzly.Training']"})
        },
        'grizzly.insurancetype': {
            'Meta': {'object_name': 'InsuranceType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'grizzly.judge': {
            'Meta': {'object_name': 'Judge'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['grizzly.JudgeType']", 'null': 'True', 'blank': 'True'})
        },
        'grizzly.judgetype': {
            'Meta': {'object_name': 'JudgeType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'grizzly.player': {
            'Meta': {'object_name': 'Player'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game_number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'insurance_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.InsuranceType']", 'null': 'True', 'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'qualification': ('django.db.models.fields.TextField', [], {}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.PlayerStatus']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.PlayerType']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'grizzly.playerstatus': {
            'Meta': {'object_name': 'PlayerStatus'},
            'body': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hosted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playerstatus_hosted_events'", 'on_delete': 'models.SET_DEFAULT', 'default': '1', 'to': "orm['contacts_and_people.Entity']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'importance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True'}),
            'in_lists': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'please_contact': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'playerstatus_person'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contacts_and_people.Person']"}),
            'publish_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'playerstatus_publish_to'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contacts_and_people.Entity']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'grizzly.playertype': {
            'Meta': {'object_name': 'PlayerType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'grizzly.rink': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Rink'},
            'birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'grizzly.team': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Team'},
            'birthday': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['grizzly.Player']", 'symmetrical': 'False'})
        },
        'grizzly.trainer': {
            'Meta': {'object_name': 'Trainer'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'grizzly.training': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Training'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'loan': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'rink': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.Rink']", 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'stop_time': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.Team']", 'null': 'True', 'blank': 'True'}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grizzly.Trainer']", 'null': 'True', 'blank': 'True'})
        },
        'links.externallink': {
            'Meta': {'ordering': "['title']", 'object_name': 'ExternalLink'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'external_site': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['links.ExternalSite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['links.LinkType']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'links.externalsite': {
            'Meta': {'ordering': "['domain']", 'object_name': 'ExternalSite'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['links.ExternalSite']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'links.linktype': {
            'Meta': {'object_name': 'LinkType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['grizzly']