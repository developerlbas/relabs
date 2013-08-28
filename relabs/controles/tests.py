"""
Control(es) la parte medular del proyecto, tiene como objetivo 
determinar las incidencias de cada uno de los trabajadores re-
gistrados para llevar el control de sus asistencias.

Ver fundamento legal.
-> Condiciones Generales de Trabajo
-> 
"""
from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from controles.models import Atributo
from controles.models import Turno
from controles.models import Control
from controles.models import Checada
from controles.models import Semana
from controles.models import TipoChecada

class TestDetectarIncidencias(TestCase):
	
	def setUp(self):
		# variable
		self.clave_de_trabajador=1110092
		self.rfc = "GAAJ780402K51"
		# Tablas relacionadas: atributo, turno
		self.atributo = Atributo.objects.create(atributo=0, descr="-vacio-")
		self.turno = Turno.objects.create(turno=1,descr="MATUTINO")
		#Insertar en tablas relacionadas: control
		self.control = Control.objects.create(clave_trabajador=self.clave_de_trabajador,rfc=self.rfc,atributo=self.atributo, turno=self.turno)
		#Dias de la semana (dia, descr)
		Semana.objects.create(dia=0, descr="Dom")
		Semana.objects.create(dia=1, descr="Lun")
		Semana.objects.create(dia=2, descr="Mar")
		Semana.objects.create(dia=3, descr="Mie")
		Semana.objects.create(dia=4, descr="Jue")
		Semana.objects.create(dia=5, descr="Vie")
		Semana.objects.create(dia=6, descr="Sab")
		
	def test_existen_datos_en_tabla_atributo(self):
		"""
		Existen datos en la tabla principal?.
		En todo caso procesar. De lo contrario, se necesita informacion
		"""
		
		try:
			obj = Atributo.objects.get(atributo=0)
			print("atributo",obj.descr)
		except ObjectDoesNotExist(e):
			print(e)
			self.assertEqual(1,0)
	
	def test_existen_datos_en_tabla_turno(self):
		"""
		La tabla turno debe tener datos
		"""
		try:
			obj = Turno.objects.get(turno=1)
			print("turno",obj.descr)
		except ObjectDoesNotExist(e):
			print(e)
			self.assertEqual(1,0)
	
	def test_existen_datos_en_tabla_control(self):
		"""
		La tabla control debe tener datos
		"""
		try:
			obj = Control.objects.get(clave_trabajador=self.clave_de_trabajador)
			print("control",obj.clave_trabajador)
		except ObjectDoesNotExist,e:
			print(e)
			self.assertEqual(1,0)
	
	def test_existen_datos_en_tabla_semana(self):
		"""
		La semana tiene 7 dias. El primero es domingo
		segun calendario
		"""
		try:
			obj = Semana.objects.get(dia=2)
		except ObjectDoesNotExist, e:
			print(e)
			self.assertEqual(0,1)
	def test_existen_datos_en_tabla_tipo_checada(self):
		"""
		Debe tener informacion antes de procesar cualquier 
		registro
		"""
		try:
			obj = TipoChecada.objects.get(tipo=1)
		except ObjectDoesNotExist, e:
			print(e)
			self.assertEqual(0,1)
			
	def test_existen_datos_en_tabla_checada(self):
		"""
		Al menos debe existir datos en la tabla checada
		"""
		try:
			obj = Checada.objects.select_related().get(clave_trabajador=self.clave_de_trabajador)
			print("checada",obj)
		except ObjectDoesNotExist, e:
			print(e)
			self.assertEqual(1,0)