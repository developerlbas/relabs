from django.db import models

from django.db import models
#------------------------------------------
class Genero(models.Model):
	sexo	= models.CharField(max_length=10, primary_key=True, null=False)
	descr	= models.CharField(max_length=25, null=False)

	class Meta:
		db_table='genero'
#------------------------------------------
class Marital(models.Model):
	estado_civil	= models.CharField(max_length=25, null=False, primary_key=True)
	descr			= models.CharField(max_length=25, null=False)

	class Meta:
		db_table='marital'
#------------------------------------------
class Nacionalidad(models.Model):
	abbr_estado		= models.CharField(max_length=5, primary_key=True, null=False)
	descr			= models.CharField(max_length=100)	
	nacimiento		= models.CharField(max_length=50)
	clave_estado	= models.IntegerField()

	class Meta:
		db_table='nacionalidad'
#------------------------------------------
class Personal(models.Model):
	rfc			= models.CharField(max_length=13, primary_key=True, null=False)
	apellidop 	= models.CharField(max_length=50, null=False)
	apellidom	= models.CharField(max_length=50, blank=True)
	nombre		= models.CharField(max_length=100, null=False)
	curp		= models.CharField(max_length=18, null=False, unique=True)
	sexo		= models.ForeignKey(Genero)
	estado_civil= models.ForeignKey(Marital)
	abbr_estado	= models.ForeignKey(Nacionalidad)
	ingreso_gob	= models.DateField(auto_now_add=False, null=False)
	ingreso_dep	= models.DateField(auto_now_add=False, null=False)
	domicilio	= models.CharField(max_length=200, blank=True, null=True)
	colonia		= models.CharField(max_length=200, blank=True, null=True)
	municipio	= models.CharField(max_length=200, blank=True, null=True)
	cedula		= models.BigIntegerField(default=0)

	class Meta:
		db_table='personal'
#------------------------------------------
class Programa(models.Model):
	tipo_trabajador	= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=50, null=False)

	class Meta:
		db_table='programa'
#------------------------------------------
class Autoridad(models.Model):
	autoridad		= models.CharField(max_length=25, null=False, primary_key=True)
	descr			= models.CharField(max_length=50, blank=True)

	class Meta:
		db_table='autoridad'
#------------------------------------------
