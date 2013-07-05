# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Personal.colonia'
        db.alter_column('personal', 'colonia', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Personal.domicilio'
        db.alter_column('personal', 'domicilio', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Personal.municipio'
        db.alter_column('personal', 'municipio', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Personal.colonia'
        db.alter_column('personal', 'colonia', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Personal.domicilio'
        db.alter_column('personal', 'domicilio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Personal.municipio'
        db.alter_column('personal', 'municipio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'repemps.adscripcion': {
            'Meta': {'object_name': 'Adscripcion', 'db_table': "'adscripcion'"},
            'cr': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fdescr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fisicamente': ('django.db.models.fields.IntegerField', [], {}),
            'jnum': ('django.db.models.fields.IntegerField', [], {})
        },
        u'repemps.autoridad': {
            'Meta': {'object_name': 'Autoridad', 'db_table': "'autoridad'"},
            'autoridad': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'repemps.codigos': {
            'Meta': {'object_name': 'Codigos', 'db_table': "'codigos'"},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rama': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'apellidom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'apellidop': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'colonia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'curp': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '18'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'default': "'CONOCIDO'", 'max_length': '200'}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Marital']"}),
            'ingreso_dep': ('django.db.models.fields.DateField', [], {}),
            'ingreso_gob': ('django.db.models.fields.DateField', [], {}),
            'municipio': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'sexo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Genero']"})
        },
        u'repemps.plantilla': {
            'Meta': {'object_name': 'Plantilla', 'db_table': "'plantilla'"},
            'activo': ('django.db.models.fields.SmallIntegerField', [], {}),
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'autoridad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Autoridad']"}),
            'clave_presupuestal': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Codigos']"}),
            'cr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Adscripcion']"}),
            'docto': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fakerfc': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'jornada': ('django.db.models.fields.SmallIntegerField', [], {}),
            'movto': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quincena': ('django.db.models.fields.IntegerField', [], {}),
            'rfc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Personal']", 'primary_key': 'True'}),
            'tabulador': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_trabajador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Programa']"}),
            'tipot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Tipot']"}),
            'vigencia_del': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'vigencial_al': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'repemps.programa': {
            'Meta': {'object_name': 'Programa', 'db_table': "'programa'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_trabajador': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        },
        u'repemps.tipot': {
            'Meta': {'object_name': 'Tipot', 'db_table': "'tipot'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        }
    }

    complete_apps = ['repemps']