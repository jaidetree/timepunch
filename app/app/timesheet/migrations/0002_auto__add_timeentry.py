# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TimeEntry'
        db.create_table('timesheet_timeentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('stop_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('category', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('timesheet', ['TimeEntry'])


    def backwards(self, orm):
        
        # Deleting model 'TimeEntry'
        db.delete_table('timesheet_timeentry')


    models = {
        'timesheet.timeentry': {
            'Meta': {'object_name': 'TimeEntry'},
            'category': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['timesheet']
