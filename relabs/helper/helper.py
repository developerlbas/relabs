#std libs
import csv
from datetime import datetime, date
#django core libs
from django.utils.timezone import utc
from django.db.utils import IntegrityError
#third-party libs
#app lib
from .models import Paso
from .excepcion import UnknownSource

"""
file = request.FILES['fileUpload']
data = [row for row in csv.reader(file)]
https://github.com/chronossc/django-data-importer/tree/master/data_importer
"""
class CSVParser(object):
	"""
	Period. Cada ingreso al sistema debera ser obtenida del reporte generado por
	el reloj checador.
	1,20130430								-> extraction data timestamp
	000000,4,20130430,&						-> first date and data (below)
	121022,3,0000022215,?,40,40,40,40,40	-> time(HHMMSS), 
											-> 3 (type of data)
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
	
	def __init__(self, archivo, **kwargs):
		"""
		init recibe archivo
		"""
		self._source = None
		self.loaded = False
		self._reader = None
		self.delimiter = kwargs.pop('delimiter',',')
		self.__load(archivo)
		#
		self.extraction_timestamp= date.today()
		self.processed_timestamp = datetime.today()

	def __load(self, source):
		"""
		Carga el archivo a "self._source". Lanza excepcion en caso de error
		"""
		try:
			if isinstance(source, file):
				self._source = source
			if isinstance(source, basestring):
				self._source = open(source, 'rb')
			self._source = source
		except Exception, err:
			raise UnknownSource(err)
			
		self.loaded = True
		self.set_reader()
		assert self._reader is not None

	def set_reader(self):
		"""
		Este...
		"""
		try:
			self._reader = csv.reader(self._source, delimiter = self.delimiter)
		except csv.Error as e:
			print "File: %s, linea: %d : %s" %(self._source, self._reader.line_num, e)

	def get_value(self, item):
		"""
		Retorna un intero si el valor es visto como entero. En otro caso,
		solo retorna el item
		"""
		try:
			int(item)
		except:	
			pass
		else:
			return int(item)
		return item

	def get_items(self):
		"""
		Recorre todo el archivo retornando los valores correspondientes.
		Al mismo tiempo verifica el tipo de informacion, almacena los
		valores en un dict para posteriormente vaciarlos en la tabla
		"""

		#truncate models
		Paso.objects.all().delete()
		
		for row in self._reader:
			if not row: continue # las lineas en blanco o invalidas se ignoran
			#la fecha de extraction. Verificar patron (1)
			if len(row) == 2:
				if 1 == self.get_value(row[0]):
					self.extraction_timestamp = datetime.strptime(row[1], '%Y%m%d').replace(tzinfo=utc)
				
			#la fecha de checada. Verificar patron (4)	
			elif len(row) == 4:
				if 4 == self.get_value(row[1]):
					fecha_de_checada = datetime.strptime(row[2], "%Y%m%d")
				
			#los datos del trabajador y hora de checada. Verificar patron (3)
			elif len(row) == 9:
				if 3 == self.get_value(row[1]):
					hora_de_checada = datetime.strptime(row[0], "%H%M%S")
					hora_de_checada = hora_de_checada.time()
					hora_y_fecha_de_checada = datetime.combine(fecha_de_checada, hora_de_checada).replace(tzinfo=utc)
					clave_de_trabajador = self.get_value(row[2])
					# insertar en tabla
					#clave_trabajador 
					#fecha_control
					#hora_control
					#actualizacion
					#id
					try:
						p = Paso(clave_trabajador=clave_de_trabajador,
							fecha_control=hora_y_fecha_de_checada,
							hora_control=hora_de_checada,
							actualizacion=self.extraction_timestamp
							)
						p.save()
					except IntegrityError:
						pass
		return True
