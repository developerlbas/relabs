# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paso'
        db.create_table('paso', (
            ('clave_trabajador', self.gf('django.db.models.fields.BigIntegerField')()),
            ('fecha_control', self.gf('django.db.models.fields.DateTimeField')()),
            ('hora_control', self.gf('django.db.models.fields.TimeField')()),
            ('actualizacion', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'helper', ['Paso'])


    def backwards(self, orm):
        # Deleting model 'Paso'
        db.delete_table('paso')


    models = {
        u'helper.paso': {
            'Meta': {'object_name': 'Paso', 'db_table': "'paso'"},
            'actualizacion': ('django.db.models.fields.DateTimeField', [], {}),
            'clave_trabajador': ('django.db.models.fields.BigIntegerField', [], {}),
            'fecha_control': ('django.db.models.fields.DateTimeField', [], {}),
            'hora_control': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['helper']