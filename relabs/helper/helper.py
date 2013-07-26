#std libs
import csv
#django core libs
from django.core.files.uploadedfile import InMemoryUploadedFile
#third-party libs
#app lib

"""
file = request.FILES['fileUpload']
data = [row for row in csv.reader(file)]
https://github.com/chronossc/django-data-importer/tree/master/data_importer
"""
class CSVParser(object):
	
	def __init__(self, archivo):
		"""
		init recibe archivo como el archivo subido
		"""