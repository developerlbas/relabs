# core libs
from django import forms
#third-party libs
# app libs
from .models import Paso

class PasoUploadModelForm(forms.ModelForm):
	
	class Meta:
		model = Chk
		
