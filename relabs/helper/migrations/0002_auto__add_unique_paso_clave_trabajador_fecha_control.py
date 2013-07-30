# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Paso', fields ['clave_trabajador', 'fecha_control']
        db.create_unique('paso', ['clave_trabajador', 'fecha_control'])


    def backwards(self, orm):
        # Removing unique constraint on 'Paso', fields ['clave_trabajador', 'fecha_control']
        db.delete_unique('paso', ['clave_trabajador', 'fecha_control'])


    models = {
        u'helper.paso': {
            'Meta': {'unique_together': "(('clave_trabajador', 'fecha_control'),)", 'object_name': 'Paso', 'db_table': "'paso'"},
            'actualizacion': ('django.db.models.fields.DateTimeField', [], {}),
            'clave_trabajador': ('django.db.models.fields.BigIntegerField', [], {}),
            'fecha_control': ('django.db.models.fields.DateTimeField', [], {}),
            'hora_control': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['helper']