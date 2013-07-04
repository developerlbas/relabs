"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#apps
from repemps.models import Plantilla

class PlantillaTestCase(TestCase):
	# datos preliminares
	def test_listado_general(self):
		p=Plantilla.object.select_related().get(rfc='AAAA112266JKL')
		
		assertEqual( len(p) ,0)
		
