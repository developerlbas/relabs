#kore
from django.conf.urls import patterns, url
#local apps
from .views import Procesar, Listado

urlpatterns = patterns('',
	#Procesa todos los registros para generar el reporte
	#general. Identificando incidencias
	# Se recomienda privado
	url(r'^procesar/$', Procesar.as_view()),
	url(r'^listado/$', Listado.as_view()),
)