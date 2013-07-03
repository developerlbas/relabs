from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Plantilla

class HomeView(DetailView):
	template_name='repemps_list.html'
	context_object_name='repemp_data'
	
	def get_object(self):
		return Plantilla.objects.select_related().get(rfc='GAAJ780402K51')
		
	def get_queryset(self):
		return Plantilla.objects.all()