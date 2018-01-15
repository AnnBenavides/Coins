from django import forms

from .models import Grupo

class GrupotForm(forms.ModelForm):

    class Meta:
        model = Grupo
        fields = ('diseno', 'modelamiento','computacion')