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
	descr			= models.CharField(max_length=100, null=False)	
	nacimiento		= models.CharField(max_length=50)
	clave_estado	= models.IntegerField(null=False)

	class Meta:
		db_table='nacionalidad'
#------------------------------------------
class Personal(models.Model):
	rfc			= models.CharField(max_length=13, primary_key=True)
	apellidop 	= models.CharField(max_length=50, null=False)
	apellidom	= models.CharField(max_length=50, default='')
	nombre		= models.CharField(max_length=100, null=False)
	curp		= models.CharField(max_length=18, null=False, unique=True)
	sexo		= models.ForeignKey(Genero)
	estado_civil= models.ForeignKey(Marital)
	abbr_estado	= models.ForeignKey(Nacionalidad)
	ingreso_gob	= models.DateField(auto_now_add=False, null=False)
	ingreso_dep	= models.DateField(auto_now_add=False, null=False)
	domicilio	= models.CharField(max_length=200, default='CONOCIDO')
	colonia		= models.CharField(max_length=200, default='')
	municipio	= models.CharField(max_length=200, default='')
	cedula		= models.BigIntegerField(default=0)

	def __unicode__(self):
		return unicode(self.rfc)

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
class Codigos(models.Model):
	codigo 		= models.CharField(max_length=10, primary_key=True)
	descr		= models.CharField(max_length=150, null=False)
	rama		= models.CharField(max_length=50)
	anio		= models.IntegerField()
	
	class Meta:
		db_table='codigos'
		#unique_together=(('codigo', 'anio'),)
#------------------------------------------
class Adscripcion(models.Model):
	cr			= models.IntegerField(primary_key=True)
	descr		= models.CharField(max_length=200)
	fisicamente	= models.IntegerField()
	fdescr		= models.CharField(max_length=200)
	jnum		= models.IntegerField()
	
	class Meta:
		db_table = 'adscripcion'
	
#------------------------------------------ tipo trabajador (evt, base, reg, etc)
class Tipot(models.Model):
	tipo	= models.CharField(max_length=25, primary_key=True)
	descr	= models.CharField(max_length=25, null=False)
	
	class Meta:
		db_table='tipot'
#------------------------------------------
class Plantilla(models.Model):
	rfc				= models.ForeignKey(Personal, primary_key=True)
	vigencia_del	= models.DateField(auto_now_add=False, null=True)
	vigencial_al	= models.DateField(auto_now_add=False, null=True)
	cr				= models.ForeignKey(Adscripcion)
	autoridad		= models.ForeignKey(Autoridad)
	activo			= models.SmallIntegerField()
	tabulador		= models.SmallIntegerField()
	jornada			= models.SmallIntegerField()
	tipo_trabajador = models.ForeignKey(Programa)
	clave_presupuestal = models.CharField(max_length=30)
	movto			= models.IntegerField(default=0)
	docto			= models.IntegerField(default=0)
	fakerfc			= models.CharField(max_length=13)
	codigo			= models.ForeignKey(Codigos)
	anio			= models.IntegerField()
	quincena 		= models.IntegerField()
	tipot			= models.ForeignKey(Tipot)
	
	#objects			= models.Manager()
	#datos			= MaleManager()
	
	def __unicode__(self):
		return self.clave_presupuestal
		
	class Meta:
		db_table='plantilla'
#-----------------------------------------