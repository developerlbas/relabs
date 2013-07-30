#std
#django core
from django.views.generic.edit import FormView
#trhid-p
#apps
from .forms import CHKFileForm

class CHKFileView(FormView):
	template_name = 'cargar.html'
	form_class = CHKFileForm
	success_url = '/tanks/'
	
	def form_valid(self, form):
		return super(CHKFileView,self).form_valid(form)
