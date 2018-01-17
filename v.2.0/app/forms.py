from django import forms
from .models import Bien, Bloque,Carga

class BienForm(forms.ModelForm):

	class Meta:
		model = Bien
		fields = ('nombre','valor',)


class BloqueForm(forms.ModelForm):

	class Meta:
		model = Bloque
		fields = ('dia','horas','valor','estado')

class CargarForm(forms.Form):
	
	class Meta:
		model = Carga
		fields = ('alumno','carga','asunto',)

