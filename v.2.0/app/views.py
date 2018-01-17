from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Grupo, Profesor, Bloque, Bien, Historial
from .forms import BienForm


# Create your views here.
def getAlumno(usuario):
	return Alumno.objects.get(user=usuario)

def getProfesor(usuario):
	return Profesor.objects.get(user=usuario)

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
	user = getProfesor(request.user)
	if (user.is_authenticated):
		alumno = get_object_or_404(Alumno, pk=pk)
		alumno.cargar(2)
		nombre = "Compra ayuda a "+str(alumno)
		h = Historial.objects.create(user=user, asunto=nombre, valor='2')
		return render(request, 'app/perfil_alumno.html', {'alumno' : alumno})
	else:
		return redirect('login.html')

def cargar(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CargarForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...



            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = CargarForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })



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