#std
#django core
from django.views.generic.edit import FormView
#trhid-p
#apps
from .csvtoint import CSVParser
from .forms import CHKFileForm


class CHKFileView(FormView):
	template_name = 'chk/cargar.html'
	form_class = CHKFileForm
	success_url = 'ctl/procesar/'
	
	def form_valid(self, form):
		return super(CHKFileView,self).form_valid(form)
		
	def form_invalid(self, form):
		return super(CHKFileView,self).form_invalid(form)
	
	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance with the passed
		POST variables and then checked for validity.
		"""
		archivo = request.FILES['archivo']
		print "[+] Try load: ", archivo, "<==>" * 20
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid:
			#Create a new CSVReader
			r = CSVParser(archivo)
			r.get_items()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
