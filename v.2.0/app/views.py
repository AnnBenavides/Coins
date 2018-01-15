from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Taller, Grupo, Profesor


# Create your views here.


def users_list(request):
	profesores = Profesor.objects.all()
	alumnos = Alumno.objects.all().order_by('taller')

	return render(request, 'app/users_list.html', {'profesores' : profesores, 'alumnos' : alumnos})

def perfil_profe(request,pk):
	profe = get_object_or_404(Profesor, pk=pk)
	return render(request, 'app/perfil_profe.html', {'profe' : profe})

def perfil_alumno(request,pk):
	alumno = get_object_or_404(Alumno, pk=pk)
	return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})