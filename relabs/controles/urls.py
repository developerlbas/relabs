#kore
from django.conf.urls import patterns, url
#local apps
from .views import Procesar

urlpatterns = patterns('',
	url(u'^procesar/$', Procesar.as_view()),
)