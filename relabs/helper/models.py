from django.db import models

# Create your models here.
class Paso(models.Model):
	"""
	Period. Cada ingreso al sistema debera ser obtenida del reporte generado por
	el reloj checador.
	1,20130430								-> extraction data timestamp
	000000,4,20130430,&						-> first date and data (below)
	121022,3,0000022215,?,40,40,40,40,40	-> time(HH:MM:SS), 
											-> 3 (type of date)
											-> ######### (clave_trabajador, 10 digits)
											-> ?, 40,40,40,40,40,40 (not used?)
	...
	000000,4,20130501,&						-> second date and data (follow)
	085500,3,0000002172,?,40,40,40,40,40	-> many records
	131236,3,0000002172,?,40,40,40,40,40	-> ...
	...
	000000,4,20130502,&
	084530,3,0001110164,?,40,40,40,40,40
	084538,3,0001110016,?,40,40,40,40,40
	084548,3,0000003091,?,40,40,40,40,40
	084748,3,0001110007,?,40,40,40,40,40
	084854,3,0001130007,?,40,40,40,40,40
	...
	patterns:
	a) 1,20130430							-> 1st field == 1 
	b) 000000,4,20130430,&					-> 2nd field == 4
	c) 121022,3,0000022215,?,40,40,40,40,40	-> 2nd field == 3
	
	Pseudo:
	clave_trabajador 	= c[2]
	fecha_control		= b[2]
	hora_control		= c[0]
	actualizacion		= a[1]
	"""
	clave_trabajador 	= models.BigIntegerField()
	fecha_control		= models.DateTimeField(auto_now_add=False)
	hora_control		= models.TimeField()
	actualizacion		= models.DateTimeField(auto_now_add=False)
	id					= models.AutoField(primary_key=True)

	class Meta:
		db_table='paso'
		unique_together= ('clave_trabajador','fecha_control')
