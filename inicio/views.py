from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inicio.forms import FormularioCrearMovil, FormularioCrearTelevisores, FormularioCrearLaptops
from inicio.models import Moviles, Televisores



def inicio(request):
   return render(request, 'inicio/inicio.html', {})


def Moviles(request):       #En esta vista voy a mostrar listado de moviles cargados
    return render(request, 'inicio/moviles.html', {})

def cargar_movil(request):  #Vista con formulario para crear movil
    
    if request.method == 'POST':
        formulario = FormularioCrearMovil(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            modelo = atributos.get('modelo')
            color = atributos.get('color')
            mpx_camara = atributos.get('mpx_camara')
            
            moviles = Moviles(marca=marca, modelo=modelo, color=color, mpx_camara=mpx_camara)
            moviles.save()
        
    formulario = FormularioCrearMovil()
    return render(request, 'inicio/cargar_movil.html', {'formulario': formulario})
    



def Televisores(request):
   return render(request, 'inicio/televisores.html', {})


def cargar_televisor(request):  #Vista con formulario para crear movil
    if request.method == 'POST':
        formulario = FormularioCrearTelevisores(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            pulgadas = atributos.get('pulgadas')
            definicion = atributos.get('definicion')
            es_smart = atributos.get('es_smart')
            
            televisor = Televisores(marca=marca, pulgadas=pulgadas, definicion=definicion, es_smart=es_smart)
            televisor.save()
        
    formulario = FormularioCrearTelevisores()
    return render(request, 'inicio/cargar_televisor.html', {'formulario': formulario})



def Laptops(request):
   return render(request, 'inicio/laptops.html', {})

def cargar_laptop(request):  #Vista con formulario para crear movil
    if request.method == 'POST':
        formulario = FormularioCrearLaptops(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            procesador = atributos.get('procesador')
            pulgadas = atributos.get('pulgadas')
                        
            laptop = Laptops(marca=marca, procesador=procesador, pulgadas=pulgadas)
            laptop.save()
        
    formulario = FormularioCrearLaptops()
    return render(request, 'inicio/cargar_laptop.html', {'formulario': formulario})