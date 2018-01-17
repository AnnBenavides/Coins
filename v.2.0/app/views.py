from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Grupo, Profesor, Bloque, Bien, Historial
from .forms import BienForm, BloqueForm


# Create your views here.
def getAlumno(usuario):
	return get_object_or_404(Alumno, user=usuario)

def getProfesor(usuario):
	return get_object_or_404(Profesor, user=usuario)

def users_list(request):
	profesores = Profesor.objects.all()
	alumnos = Alumno.objects.all().order_by('grupo')
	bienes = Bien.objects.all()
	user = request.user
	if (user.is_authenticated):
		return render(request, 'app/users_list.html', {'profesores' : profesores, 'alumnos' : alumnos, 'bienes' : bienes})
	else:
		return redirect('login.html')
def perfil_profe(request,pk):
	profe = get_object_or_404(Profesor, pk=pk)
	bloques = Bloque.objects.filter(profe=profe).order_by('dia')
	user = request.user
	if (user.is_authenticated):
		return render(request, 'app/perfil_profe.html', {'profe' : profe, 'bloques':bloques})
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
	user = getProfesor(request.user)
	if (user.is_authenticated):
		alumno = get_object_or_404(Alumno, pk=pk)
		alumno.cargar(2)
		nombre = "Compra ayuda a "+str(alumno)
		h = Historial.objects.create(user=user, asunto=nombre, valor='2')
		return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})
	else:
		return redirect('login.html')

def bien(request,pk):
	bien = get_object_or_404(Bien, pk=pk)
	if (user.is_authenticated):
		alumno = getAlumno(request.user)
		alumno.cargar(bien.valor)
		nombre = "Compra de bien "+str(alumno)
		h = Historial.objects.create(user=request.user, asunto=nombre, valor=bien.valor)
		return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})
	else:
		return redirect('login.html')

def nuevo_bien(request):
	if request.method == "POST":
		form = BienForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			profe = getProfesor(request.user)
			h = Historial.objects.create(user=request.user, asunto='Crear bien', valor='0')
			post.save()
			return render(request, 'app/perfil_profe.html', {'profe' : profe})
	else:
		form = BienForm()
		return render(request,'app/nuevo_bien.html', {'form':form})

def nuevo_bloque(request):
	if request.method == "POST":
		form = BloqueForm(request.POST)
		if form.is_valid():
			bloque = form.save(commit=False)
			bloque.profe = getProfesor(request.user)
			bloque.grupo = 0
			bloque.save()
			h = Historial.objects.create(user=request.user, asunto='Crear bloque', valor=bloque.valor)
			return render(request, 'app/perfil_profe.html', {'profe' : bloque.profe})
	else:
		form = BloqueForm()
		return render(request, 'app/nuevo_bloque.html', {'form':form})

def ediar_bloque(request,pk):
	bloque = get_object_or_404(Bloque, pk=pk)
	if request.method == "POST":
		form = BloqueForm(request.POST, intance=bloque)
		if form.is_valid():
			bloque = form.save(commit=False)
			bloque.profe = getProfesor(request.user)
			bloque.grupo = 0
			bloque.save()
			h = Historial.objects.create(user=request.user, asunto='Cambio en bloque', valor=bloque.valor)
			return render(request, 'app/perfil_profe.html', {'profe' : bloque.profe})
	else:
		form = BloqueForm()
		return render(request, 'app/nuevo_bloque.html', {'form':form})


def comprar_bloque(request,pk):
	bloque = get_object_or_404(Bloque, pk=pk)
	if (user.is_authenticated):
		alumno = getAlumno(request.user)
		alumno.cargar(bien.valor)
		bloque.comprado(alumno.grupo)
		nombre = "Compra bloque "+str(bloque.profe)
		h = Historial.objects.create(user=request.user, asunto=nombre, valor=bloque.valor)
		return render(request, 'app/perfil_profe.html', {'profe' : bloque.profe})
	else:
		return redirect('login.html')

def bloque_ausente(request,pk):
	bloque = get_object_or_404(Bloque, pk=pk)
	if (user.is_authenticated):
		profe = getProfe(request.user)
		bloque.ausente()
		nombre = "Bloque ausente"
		h = Historial.objects.create(user=request.user, asunto=nombre, valor='0')
		return render(request, 'app/perfil_profe.html', {'profe' : profe})
	else:
		return redirect('login.html')