from django.shortcuts import render
from .models import Alumno, Taller, Grupo, Profesor

# Create your views here.

def users_list(request):
	profesores = Profesor.objects.all()
	return render(request, 'app/users_list.html', {'profesores' : profesores})