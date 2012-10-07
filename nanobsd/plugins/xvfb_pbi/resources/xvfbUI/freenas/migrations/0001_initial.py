# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Xvfb'
        db.create_table('freenas_xvfb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('x11_DISPLAY', self.gf('django.db.models.fields.CharField')(default=':1', max_length=500, blank=False)),
            ('xvfb_enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('xvfbservices_list', self.gf('django.db.models.fields.CharField')(default='', max_length=12)),
        ))
        db.send_create_signal('freenas', ['Xvfb'])


    def backwards(self, orm):
        # Deleting model 'Xvfb'
        db.delete_table('freenas_xvfb')


    models = {
        'freenas.xvfb': {
            'Meta': {'object_name': 'Xvfb'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
