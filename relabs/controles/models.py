"""
	PEP 8 describes coding conventions such as:
	*> Use 4 spaces per indentation level.
	*> Separate top-level function and class definitions with two blank lines.
	*> Method definitions inside a class are separated by a single blank line.

	1. Standard library imports. 
	2. Imports from core Django. 
	3. Imports from third-party apps. 
	4. Imports from the apps that you created as part of your Django project.
"""
#core django
from django.db import models
from django.contrib.auth.models import User
# local apps
from repemps.models import Plantilla


class Turno(models.Model):
	"""
	Cada trabajador tiene un turno laboral. Este puede ser matutino, ves-
	pertino, nocturno o especial.
	Por default, el turno sera matutino
	"""
	turno		= models.SmallIntegerField(primary_key=True)
	descr		= models.CharField(max_length=50, null=False)

	class Meta:
		db_table='turno'

class Atributo(models.Model):
	"""
	Atributo del trabajador. Estos pueden ser aquellos  atributos que por su
	naturaleza no se encuentran contemplados en datos Personales. Tales  ---
	atributos son, no limitados a : parentesco (PADRE o MADRE), delegacion a
	la que pertenecen, etc.
	"""
	atributo	= models.SmallIntegerField(primary_key=True)
	descr		= models.CharField(max_length=50)

	class Meta:
		db_table='atributo'

class Control(models.Model):
	"""
	Controla el personal que sera procesado. Es decir, este control la relacion
	clave_trabajador <-> rfc. Opcionalmente se agrega el atributo y turno del -
	trabajador.
	"""
	clave_trabajador	= models.BigIntegerField(primary_key=True)
	rfc					= models.ForeignKey(Plantilla)
	atributo			= models.ForeignKey(Atributo)
	turno				= models.ForeignKey(Turno)

	class Meta:
		db_table='control'


class Semana(models.Model):
	"""
	Describe los dias de la semana laboral. Se identifican como lo establece el
	calendario ingles. 0 es domingo, 1 es lunes...asi sucesivamente.
	"""
	dia			= models.SmallIntegerField(primary_key=True)
	descr		= models.CharField(max_length=50)

	class Meta:
		db_table='semana'


class TipoChecada(models.Model):
	"""
	Se refiere a que turno-hora checa.
	Por ejemplo, la hora de entrada matutina se refleja como 1,
	la salida matutina 2,
	la entrada vespertina 3,
	la salida vespertina 4
	"""
	tipo		= models.SmallIntegerField(primary_key=True)
	descr		= models.CharField(max_length=50)

	class Meta:
		db_table='tipo_checada'


class Horario(models.Model):
	"""
	Cada trabajador tiene un horario de acuerdo a sus necesidades y de acuerdo -
	al programa al que pertenece (eventual, regularizado, base, etc.)
	"""
	clave_trabajador 	= models.ForeignKey(Control)
	dia_de_semana		= models.ForeignKey(Semana)
	hora				= models.TimeField()
	habilitado			= models.SmallIntegerField()
	tipo_checada		= models.ForeignKey(TipoChecada)
	#id					= models.AutoField()

	class Meta:
		db_table = 'horario'
		unique_together = ('clave_trabajador', 'dia_de_semana')


class Operacion(models.Model):
	"""
	Operacion es un catalogo de incidentes que puede tener un trabajador. Por -
	ejemplo, el catalogo de pagos _movimientos_ establece como 7230 una falta -
	injustificada. Las vacaciones se incluiran con la "mayor" jerarquia posible,
	pues es el unico que tiene mayor precedencia (hierarchy). Etapa de revision.
	Atencion:
	Esta en etapa de revision.
	grupo se refiere al tipo de incidencia, puede ser grupo vacaciones, grupo --
	permisos generales, grupo licencias, etc.
	jerarquia va de a mano con la operacion. Se tiene contemplado aunque resulta
	duplicidad con operacion.
	"""
	operacion		= models.IntegerField(primary_key=True)
	short_descr		= models.CharField(max_length=10)
	long_descr		= models.CharField(max_length=100)
	grupo			= models.SmallIntegerField()
	jerarquia		= models.SmallIntegerField()
	habilitado		= models.BooleanField()

	class Meta:
		db_table='operacion'


class Excepcion(models.Model):
	"""
	En algunas ocasiones, sobre todo los dias festivos, permisos por parte sin-
	dical, permisos por dia del padre, de tu madre (:P),deberan ser exceptuados.
	"""
	fecha_excepcion		= models.DateField()
	descr				= models.CharField(max_length=100)
	hora_excepcion		= models.TimeField()
	operacion			= models.ForeignKey(Operacion)
	habilitado			= models.BooleanField()
	
	class Meta:
		db_table = 'excepcion' # tambien podria ser nombrado fetivos


class Checada(models.Model):
	"""
	Period. Cada ingreso al sistema debera ser obtenida del reporte generado por
	el reloj checador.
	Opcionalmente se tiene pensado usar una tabla temporal donde se generan para
	cada trabajador los dias de la semana que labora, esto con la finalidad de -
	tener un layout fuerte. eliminado claro, aquellas execpciones, y los dias no
	laborales por el determinado trabajador.
	"""
	clave_trabajador 	= models.ForeignKey(Control)
	fecha_control		= models.DateField()
	hora_control		= models.TimeField()
	observaciones		= models.CharField(max_length=200)
	habilitado			= models.BooleanField()
	operacion			= models.ForeignKey(Operacion)
	usuario				= models.ForeignKey(User)
	id					= models.AutoField(primary_key=True)

	class Meta:
		db_table='checada'