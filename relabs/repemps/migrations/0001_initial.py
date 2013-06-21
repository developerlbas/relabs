# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genero'
        db.create_table('genero', (
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'repemps', ['Genero'])

        # Adding model 'Marital'
        db.create_table('marital', (
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'repemps', ['Marital'])

        # Adding model 'Nacionalidad'
        db.create_table('nacionalidad', (
            ('abbr_estado', self.gf('django.db.models.fields.CharField')(max_length=5, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nacimiento', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('clave_estado', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'repemps', ['Nacionalidad'])

        # Adding model 'Personal'
        db.create_table('personal', (
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=13, primary_key=True)),
            ('apellidop', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidom', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('curp', self.gf('django.db.models.fields.CharField')(unique=True, max_length=18)),
            ('sexo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Genero'])),
            ('estado_civil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Marital'])),
            ('abbr_estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Nacionalidad'])),
            ('ingreso_gob', self.gf('django.db.models.fields.DateField')()),
            ('ingreso_dep', self.gf('django.db.models.fields.DateField')()),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cedula', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal(u'repemps', ['Personal'])

        # Adding model 'Programa'
        db.create_table('programa', (
            ('tipo_trabajador', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'repemps', ['Programa'])

        # Adding model 'Autoridad'
        db.create_table('autoridad', (
            ('autoridad', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'repemps', ['Autoridad'])

        # Adding model 'Plantilla'
        db.create_table('plantilla', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rfc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Personal'])),
            ('tipo_trabajador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Programa'])),
        ))
        db.send_create_signal(u'repemps', ['Plantilla'])


    def backwards(self, orm):
        # Deleting model 'Genero'
        db.delete_table('genero')

        # Deleting model 'Marital'
        db.delete_table('marital')

        # Deleting model 'Nacionalidad'
        db.delete_table('nacionalidad')

        # Deleting model 'Personal'
        db.delete_table('personal')

        # Deleting model 'Programa'
        db.delete_table('programa')

        # Deleting model 'Autoridad'
        db.delete_table('autoridad')

        # Deleting model 'Plantilla'
        db.delete_table('plantilla')


    models = {
        u'repemps.autoridad': {
            'Meta': {'object_name': 'Autoridad', 'db_table': "'autoridad'"},
            'autoridad': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'repemps.genero': {
            'Meta': {'object_name': 'Genero', 'db_table': "'genero'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'repemps.marital': {
            'Meta': {'object_name': 'Marital', 'db_table': "'marital'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        },
        u'repemps.nacionalidad': {
            'Meta': {'object_name': 'Nacionalidad', 'db_table': "'nacionalidad'"},
            'abbr_estado': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'}),
            'clave_estado': ('django.db.models.fields.IntegerField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'repemps.personal': {
            'Meta': {'object_name': 'Personal', 'db_table': "'personal'"},
            'abbr_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Nacionalidad']"}),
            'apellidom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'apellidop': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '18'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Marital']"}),
            'ingreso_dep': ('django.db.models.fields.DateField', [], {}),
            'ingreso_gob': ('django.db.models.fields.DateField', [], {}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'sexo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Genero']"})
        },
        u'repemps.plantilla': {
            'Meta': {'object_name': 'Plantilla', 'db_table': "'plantilla'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rfc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Personal']"}),
            'tipo_trabajador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Programa']"})
        },
        u'repemps.programa': {
            'Meta': {'object_name': 'Programa', 'db_table': "'programa'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_trabajador': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        }
    }

    complete_apps = ['repemps']