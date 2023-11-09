from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from inicio.forms import FormularioCrearMovil, FormularioCrearTelevisores, FormularioCrearLaptops
from inicio.models import Moviles, Televisores, Laptops



def inicio(request):
   return render(request, 'inicio/inicio.html', {})


# ==================== MOVILES =====================

def Moviles_principal(request):       #En esta vista voy a mostrar listado de moviles cargados
    
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_moviles = Moviles.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_moviles = Moviles.objects.all()

    return render(request, 'inicio/moviles.html', {'listado_moviles': listado_moviles})


def cargar_movil(request):  #Vista con formulario para crear movil
    if request.method == 'POST':
        formulario = FormularioCrearMovil(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            modelo = atributos.get('modelo')
            color = atributos.get('color')
            mpx_camara = atributos.get('mpx_camara')
            
            movil = Moviles(marca=marca.lower(), modelo=modelo, color=color, mpx_camara=mpx_camara)
            movil.save()
            
            return redirect('moviles')
        else:
            return render(request, 'inicio/cargar_movil.html', {'formulario': formulario})
    formulario = FormularioCrearMovil()
    return render(request, 'inicio/cargar_movil.html', {'formulario': formulario})
    

# ==================== TELEVISORES =====================

def Televisores_principal(request):
    
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_televisores = Televisores.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_televisores = Televisores.objects.all()
     
    return render(request, 'inicio/televisores.html', {'listado_televisores':listado_televisores})


def cargar_televisor(request):  #Vista con formulario para crear movil
    if request.method == 'POST':
        formulario = FormularioCrearTelevisores(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            pulgadas = atributos.get('pulgadas')
            definicion = atributos.get('definicion')
            es_smart = atributos.get('es_smart')
            
            televisor = Televisores(marca=marca.lower(), pulgadas=pulgadas, definicion=definicion, es_smart=es_smart)
            televisor.save()
            
            return redirect('televisores')
        else:
            return render(request, 'inicio/cargar_televisor.html', {'formulario': formulario})
    
    formulario = FormularioCrearTelevisores()
    return render(request, 'inicio/cargar_televisor.html', {'formulario': formulario})


# ==================== LAPTOPS =====================

def Laptops_principal(request):
   
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_laptops = Laptops.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_laptops = Laptops.objects.all() 
    return render(request, 'inicio/laptops.html', {'listado_laptops': listado_laptops})

def cargar_laptop(request):  #Vista con formulario para crear movil
    if request.method == 'POST':
        formulario = FormularioCrearLaptops(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            procesador = atributos.get('procesador')
            pulgadas = atributos.get('pulgadas')
                        
            laptop = Laptops(marca=marca.lower(), procesador=procesador, pulgadas=pulgadas)
            laptop.save()
            
            return redirect('laptops')
        else:
            return render(request, 'inicio/cargar_laptop.html', {'formulario': formulario})
        
    formulario = FormularioCrearLaptops()
    return render(request, 'inicio/cargar_laptop.html', {'formulario': formulario})