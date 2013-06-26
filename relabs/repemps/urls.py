from django.conf.urls import patterns, url

from .views import HomeView

urlpatterns = patterns('',
	# by rfc
	url(r'^(?P<rfc>[A-Z]{4}[0-9]{6}[A-Z0-9]{3})/$', HomeView.as_view()),
)
