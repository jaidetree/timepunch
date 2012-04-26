# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'TimeEntry.category'
        db.alter_column('timesheet_timeentry', 'category', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'TimeEntry.category'
        db.alter_column('timesheet_timeentry', 'category', self.gf('django.db.models.fields.TextField')())


    models = {
        'timesheet.timeentry': {
            'Meta': {'ordering': "['-start_time']", 'object_name': 'TimeEntry'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['timesheet']
