# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipot'
        db.create_table('tipot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'repemps', ['Tipot'])

        # Adding model 'Adscripcion'
        db.create_table('adscripcion', (
            ('cr', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fisicamente', self.gf('django.db.models.fields.IntegerField')()),
            ('fdescr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('jnum', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'repemps', ['Adscripcion'])

        # Adding model 'Codigos'
        db.create_table('codigos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('rama', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'repemps', ['Codigos'])

        # Adding unique constraint on 'Codigos', fields ['codigo', 'anio']
        db.create_unique('codigos', ['codigo', 'anio'])

        # Deleting field 'Plantilla.id'
        db.delete_column('plantilla', 'id')

        # Adding field 'Plantilla.vigencia_del'
        db.add_column('plantilla', 'vigencia_del',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Plantilla.vigencial_al'
        db.add_column('plantilla', 'vigencial_al',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Plantilla.cr'
        db.add_column('plantilla', 'cr',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['repemps.Adscripcion']),
                      keep_default=False)

        # Adding field 'Plantilla.autoridad'
        db.add_column('plantilla', 'autoridad',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['repemps.Autoridad']),
                      keep_default=False)

        # Adding field 'Plantilla.activo'
        db.add_column('plantilla', 'activo',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Plantilla.tabulador'
        db.add_column('plantilla', 'tabulador',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=2),
                      keep_default=False)

        # Adding field 'Plantilla.jornada'
        db.add_column('plantilla', 'jornada',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=8),
                      keep_default=False)

        # Adding field 'Plantilla.clave_presupuestal'
        db.add_column('plantilla', 'clave_presupuestal',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Plantilla.movto'
        db.add_column('plantilla', 'movto',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Plantilla.docto'
        db.add_column('plantilla', 'docto',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Plantilla.fakerfc'
        db.add_column('plantilla', 'fakerfc',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=13),
                      keep_default=False)

        # Adding field 'Plantilla.codigo'
        db.add_column('plantilla', 'codigo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['repemps.Codigos']),
                      keep_default=False)

        # Adding field 'Plantilla.anio'
        db.add_column('plantilla', 'anio',
                      self.gf('django.db.models.fields.IntegerField')(default=2013),
                      keep_default=False)

        # Adding field 'Plantilla.quincena'
        db.add_column('plantilla', 'quincena',
                      self.gf('django.db.models.fields.IntegerField')(default=13),
                      keep_default=False)

        # Adding field 'Plantilla.tipot'
        db.add_column('plantilla', 'tipot',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['repemps.Tipot']),
                      keep_default=False)


        # Changing field 'Plantilla.rfc'
        db.alter_column('plantilla', 'rfc_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Personal'], primary_key=True))
        # Adding unique constraint on 'Plantilla', fields ['rfc']
        db.create_unique('plantilla', ['rfc_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Plantilla', fields ['rfc']
        db.delete_unique('plantilla', ['rfc_id'])

        # Removing unique constraint on 'Codigos', fields ['codigo', 'anio']
        db.delete_unique('codigos', ['codigo', 'anio'])

        # Deleting model 'Tipot'
        db.delete_table('tipot')

        # Deleting model 'Adscripcion'
        db.delete_table('adscripcion')

        # Deleting model 'Codigos'
        db.delete_table('codigos')

        # Adding field 'Plantilla.id'
        db.add_column('plantilla', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'Plantilla.vigencia_del'
        db.delete_column('plantilla', 'vigencia_del')

        # Deleting field 'Plantilla.vigencial_al'
        db.delete_column('plantilla', 'vigencial_al')

        # Deleting field 'Plantilla.cr'
        db.delete_column('plantilla', 'cr_id')

        # Deleting field 'Plantilla.autoridad'
        db.delete_column('plantilla', 'autoridad_id')

        # Deleting field 'Plantilla.activo'
        db.delete_column('plantilla', 'activo')

        # Deleting field 'Plantilla.tabulador'
        db.delete_column('plantilla', 'tabulador')

        # Deleting field 'Plantilla.jornada'
        db.delete_column('plantilla', 'jornada')

        # Deleting field 'Plantilla.clave_presupuestal'
        db.delete_column('plantilla', 'clave_presupuestal')

        # Deleting field 'Plantilla.movto'
        db.delete_column('plantilla', 'movto')

        # Deleting field 'Plantilla.docto'
        db.delete_column('plantilla', 'docto')

        # Deleting field 'Plantilla.fakerfc'
        db.delete_column('plantilla', 'fakerfc')

        # Deleting field 'Plantilla.codigo'
        db.delete_column('plantilla', 'codigo_id')

        # Deleting field 'Plantilla.anio'
        db.delete_column('plantilla', 'anio')

        # Deleting field 'Plantilla.quincena'
        db.delete_column('plantilla', 'quincena')

        # Deleting field 'Plantilla.tipot'
        db.delete_column('plantilla', 'tipot_id')


        # Changing field 'Plantilla.rfc'
        db.alter_column('plantilla', 'rfc_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Personal']))

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
            'Meta': {'unique_together': "(('codigo', 'anio'),)", 'object_name': 'Codigos', 'db_table': "'codigos'"},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['repemps']