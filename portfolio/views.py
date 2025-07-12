from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm

def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def aboutme(request):
    return render(request, 'portfolio/aboutme.html')

def listaProyectos(request):
    Proyectos = Proyecto.objects.all()
    return render(request, 'portfolio/listaproyectos.html', {'proyectos':Proyectos})

def crear_proyectos(request):
    if request.method == 'POST':
        form =ProyectoForm(request-POST)
        if form.is_valid():
            form.save()
            return redirect('listaProyectos')
    else:
        form = ProyectoForm()
    return render(request, 'portfolio/formulario.html', {'form' : form})

def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listarProyectos')
    return render(request, 'portfolio/confirmar_eliminar.html', {'proyecto' : proyecto})

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        proyecto.delete()
        return redirect('listaProyectos')  

    return render(request, 'portfolio/confirmar_eliminar.html', {'proyecto': proyecto})