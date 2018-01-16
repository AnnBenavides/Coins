from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Grupo, Profesor, Bloque, Bien, Historial


# Create your views here.


def users_list(request):
	profesores = Profesor.objects.all()
	alumnos = Alumno.objects.all()
	user = request.user
	if (user.is_authenticated):
		return render(request, 'app/users_list.html', {'profesores' : profesores, 'alumnos' : alumnos})
	else:
		return redirect('login.html')
def perfil_profe(request,pk):
	profe = get_object_or_404(Profesor, pk=pk)
	user = request.user
	if (user.is_authenticated):
		return render(request, 'app/perfil_profe.html', {'profe' : profe})
	else:
		return redirect('login.html')
	
def perfil_alumno(request,pk):
	alumno = get_object_or_404(Alumno, pk=pk)
	user = request.user
	if (user.is_authenticated):
		return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})
	else:
		return redirect('login.html')
	
def ayuda(request,pk):
	user = request.user
	if (user.is_authenticated):
		alumno = get_object_or_404(Alumno, pk=pk)
		alumno.cargar(2)
		nombre = "Compra ayuda a "+str(alumno)
		h = Historial.objects.create(user=user, asunto=nombre, valor='2')
		return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})
	else:
		return redirect('login.html')

	