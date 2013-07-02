from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Plantilla

class HomeView(DetailView):
	template_name='repemps_list.html'
	
	def get_queryset(self):
		"""
		Return the reference object.
		"""
		rfc = self.kwargs.get('rfc')
		print "Lookup for rfc=%s" % (rfc)
		print "-------------------"
		return get_object_or_404(Plantilla, pk=rfc)
		