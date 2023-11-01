from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inicio.forms import FormularioCrearMovil



def inicio(request):
   return render(request, 'inicio/inicio.html', {})


def Moviles(request):       #En esta vista voy a mostrar listado de moviles cargados
    return render(request, 'inicio/moviles.html', {})

def cargar_movil(request):  #Vista con formulario para crear movil
    
    if request.method == 'POST':
        ...
        
    formulario = FormularioCrearMovil()
    
    return render(request, 'inicio/cargar_movil.html', {'formulario': formulario})
    



def Televisores(request):
   return render(request, 'inicio/televisores.html', {})


def Laptops(request):
   return render(request, 'inicio/laptops.html', {})