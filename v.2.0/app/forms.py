from django import forms
from .models import Bien

class BienForm(forms.ModelForm):

	class Meta:
		model = Bien
		fields = ('nombre','valor',)
