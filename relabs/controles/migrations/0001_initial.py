# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Turno'
        db.create_table('turno', (
            ('turno', self.gf('django.db.models.fields.SmallIntegerField')(primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'controles', ['Turno'])

        # Adding model 'Atributo'
        db.create_table('atributo', (
            ('atributo', self.gf('django.db.models.fields.SmallIntegerField')(primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'controles', ['Atributo'])

        # Adding model 'Control'
        db.create_table('control', (
            ('clave_trabajador', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('rfc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repemps.Plantilla'])),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Atributo'])),
            ('turno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Turno'])),
        ))
        db.send_create_signal(u'controles', ['Control'])

        # Adding model 'Semana'
        db.create_table('semana', (
            ('dia', self.gf('django.db.models.fields.SmallIntegerField')(primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'controles', ['Semana'])

        # Adding model 'TipoChecada'
        db.create_table('tipo_checada', (
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'controles', ['TipoChecada'])

        # Adding model 'Horario'
        db.create_table('horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave_trabajador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Control'])),
            ('dia_de_semana', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Semana'])),
            ('hora', self.gf('django.db.models.fields.TimeField')()),
            ('habilitado', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tipo_checada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.TipoChecada'])),
        ))
        db.send_create_signal(u'controles', ['Horario'])

        # Adding unique constraint on 'Horario', fields ['clave_trabajador', 'dia_de_semana']
        db.create_unique('horario', ['clave_trabajador_id', 'dia_de_semana_id'])

        # Adding model 'Operacion'
        db.create_table('operacion', (
            ('operacion', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('short_descr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('long_descr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grupo', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('jerarquia', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('habilitado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Operacion'])

        # Adding model 'Excepcion'
        db.create_table('excepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_excepcion', self.gf('django.db.models.fields.DateField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hora_excepcion', self.gf('django.db.models.fields.TimeField')()),
            ('operacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Operacion'])),
            ('habilitado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Excepcion'])

        # Adding model 'Checada'
        db.create_table('checada', (
            ('clave_trabajador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Control'])),
            ('fecha_control', self.gf('django.db.models.fields.DateField')()),
            ('hora_control', self.gf('django.db.models.fields.TimeField')()),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('habilitado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('operacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Operacion'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'controles', ['Checada'])


    def backwards(self, orm):
        # Removing unique constraint on 'Horario', fields ['clave_trabajador', 'dia_de_semana']
        db.delete_unique('horario', ['clave_trabajador_id', 'dia_de_semana_id'])

        # Deleting model 'Turno'
        db.delete_table('turno')

        # Deleting model 'Atributo'
        db.delete_table('atributo')

        # Deleting model 'Control'
        db.delete_table('control')

        # Deleting model 'Semana'
        db.delete_table('semana')

        # Deleting model 'TipoChecada'
        db.delete_table('tipo_checada')

        # Deleting model 'Horario'
        db.delete_table('horario')

        # Deleting model 'Operacion'
        db.delete_table('operacion')

        # Deleting model 'Excepcion'
        db.delete_table('excepcion')

        # Deleting model 'Checada'
        db.delete_table('checada')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'controles.atributo': {
            'Meta': {'object_name': 'Atributo', 'db_table': "'atributo'"},
            'atributo': ('django.db.models.fields.SmallIntegerField', [], {'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'controles.checada': {
            'Meta': {'object_name': 'Checada', 'db_table': "'checada'"},
            'clave_trabajador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Control']"}),
            'fecha_control': ('django.db.models.fields.DateField', [], {}),
            'habilitado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hora_control': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Operacion']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'controles.control': {
            'Meta': {'object_name': 'Control', 'db_table': "'control'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Atributo']"}),
            'clave_trabajador': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'rfc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repemps.Plantilla']"}),
            'turno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Turno']"})
        },
        u'controles.excepcion': {
            'Meta': {'object_name': 'Excepcion', 'db_table': "'excepcion'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_excepcion': ('django.db.models.fields.DateField', [], {}),
            'habilitado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hora_excepcion': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Operacion']"})
        },
        u'controles.horario': {
            'Meta': {'unique_together': "(('clave_trabajador', 'dia_de_semana'),)", 'object_name': 'Horario', 'db_table': "'horario'"},
            'clave_trabajador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Control']"}),
            'dia_de_semana': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Semana']"}),
            'habilitado': ('django.db.models.fields.SmallIntegerField', [], {}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_checada': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.TipoChecada']"})
        },
        u'controles.operacion': {
            'Meta': {'object_name': 'Operacion', 'db_table': "'operacion'"},
            'grupo': ('django.db.models.fields.SmallIntegerField', [], {}),
            'habilitado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jerarquia': ('django.db.models.fields.SmallIntegerField', [], {}),
            'long_descr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operacion': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'short_descr': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'controles.semana': {
            'Meta': {'object_name': 'Semana', 'db_table': "'semana'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dia': ('django.db.models.fields.SmallIntegerField', [], {'primary_key': 'True'})
        },
        u'controles.tipochecada': {
            'Meta': {'object_name': 'TipoChecada', 'db_table': "'tipo_checada'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'primary_key': 'True'})
        },
        u'controles.turno': {
            'Meta': {'object_name': 'Turno', 'db_table': "'turno'"},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'turno': ('django.db.models.fields.SmallIntegerField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['controles']