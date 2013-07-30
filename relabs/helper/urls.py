#std
#core
from django.conf.urls import patterns, url
#3rd-p
#apss
from .views import CHKFileView

urlpatterns = patterns('',
	url(u'^upload/$', CHKFileView.as_view()),
)
