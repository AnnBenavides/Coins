from django import forms
from .models import Bien, Bloque

class BienForm(forms.ModelForm):

	class Meta:
		model = Bien
		fields = ('nombre','valor',)


class BlockForm(forms.ModelForm):

	class Meta:
		model = Bloque
		fields = ('dia','horas','valor','estado')
		
