from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Plantilla

class HomeView(DetailView):
	template_name='repemps_list.html'
	context_object_name='repemp_data'
	
	def get_object(self):
		rfcpk = self.kwargs.get('rfc')
		print "Lookup object: %s " % rfcpk
		return get_object_or_404(Plantilla, rfc = rfcpk)
