from django.test import TestCase
try:
	from helper.models import Puro
except ImportError,e:
	print e


class TestIncidencias(TestCase):
	def setUp(self):
		self.me = Puro.objects.filter(clave_trabajador=1110092)
	def test_retardo_menor(self):
		"""
		Retardo menor si esta dentro de los minutos 15
		y 40. 
		"""
		print self.me	
		
