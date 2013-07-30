#std
#core
from django.forms import forms
#3rd
#apps

class CHKFileForm(forms.Form):
	archivo 	= forms.FileField()
	
