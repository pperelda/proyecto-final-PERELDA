from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from inicio.forms import FormularioCrearMovil, FormularioCrearTelevisor, FormularioCrearLaptop
from inicio.forms import FormularioEditarMovil, FormularioEditarTelevisor, FormularioEditarLaptop
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

def eliminar_movil(request, movil_id):
    movil_a_eliminar = Moviles.objects.get(id=movil_id)
    movil_a_eliminar.delete()
    return redirect('moviles')        

def editar_movil(request, movil_id):
    movil_a_editar = Moviles.objects.get(id=movil_id)
    
    if request.method == "POST":
        formulario = FormularioEditarMovil(request.POST)
        if formulario.is_valid():
            
            nuevos_atributos = formulario.cleaned_data
            
            movil_a_editar.marca = nuevos_atributos.get('marca') 
            movil_a_editar.modelo = nuevos_atributos.get('modelo')
            movil_a_editar.color = nuevos_atributos.get('color')
            movil_a_editar.mpx_camara = nuevos_atributos.get('mpx_camara')
            movil_a_editar.save()
            return redirect('moviles')
        else:
            return render(request, 'inicio/editar_movil.html', {'formulario': formulario})
    
    formulario = FormularioEditarMovil(initial={'marca':movil_a_editar.marca, 'modelo':movil_a_editar.modelo, 'color':movil_a_editar.color, 'mpx_camara':movil_a_editar.mpx_camara})
    return render(request,'inicio/editar_movil.html', {'formulario': formulario})

def detalle_movil(request, movil_id):
    movil = Moviles.objects.get(id=movil_id)
    return render(request, 'inicio/detalle_movil.html', {'movil': movil})
    
    
       
    
    
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
        formulario = FormularioCrearTelevisor(request.POST) 
        if formulario.is_valid():
            atributos = formulario.cleaned_data
            
            marca = atributos.get('marca')
            pulgadas = atributos.get('pulgadas')
            definicion = atributos.get('definicion')
            es_smart = atributos.get('es_smart')
            
            televisor = Televisores(marca=marca.upper(), pulgadas=pulgadas, definicion=definicion, es_smart=es_smart)
            televisor.save()
            
            return redirect('televisores')
        else:
            return render(request, 'inicio/cargar_televisor.html', {'formulario': formulario})
    
    formulario = FormularioCrearTelevisor()
    return render(request, 'inicio/cargar_televisor.html', {'formulario': formulario})

def eliminar_televisor(request, televisor_id):
    televisor_a_eliminar = Televisores.objects.get(id=televisor_id)
    televisor_a_eliminar.delete()
    return redirect('televisores') 

def editar_televisor(request, televisor_id):
    televisor_a_editar = Televisores.objects.get(id=televisor_id)
    
    if request.method == "POST":
        formulario = FormularioEditarTelevisor(request.POST)
        if formulario.is_valid():
            
            nuevos_atributos = formulario.cleaned_data
            
            televisor_a_editar.marca = nuevos_atributos.get('marca') 
            televisor_a_editar.pulgadas = nuevos_atributos.get('pulgadas')
            televisor_a_editar.definicion = nuevos_atributos.get('definicion')
            televisor_a_editar.es_smart = nuevos_atributos.get('es_smart')
            televisor_a_editar.save()
            return redirect('televisores')
        else:
            return render(request, 'inicio/editar_televisor.html', {'formulario': formulario})
    
    formulario = FormularioEditarTelevisor(initial={'marca':televisor_a_editar.marca.upper(), 'pulgadas':televisor_a_editar.pulgadas, 'definicion':televisor_a_editar.definicion, 'es_smart':televisor_a_editar.es_smart.upper()})
    return render(request,'inicio/editar_televisor.html', {'formulario': formulario}) 

def detalle_televisor(request, televisor_id):
    televisor = Televisores.objects.get(id=televisor_id)
    return render(request, 'inicio/detalle_televisor.html', {'televisor': televisor})


# ==================== LAPTOPS =====================

def Laptops_principal(request):
   
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_laptops = Laptops.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_laptops = Laptops.objects.all() 
    return render(request, 'inicio/laptops.html', {'listado_laptops': listado_laptops})

def cargar_laptop(request):  
    if request.method == 'POST':
        formulario = FormularioCrearLaptop(request.POST) 
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
        
    formulario = FormularioCrearLaptop()
    return render(request, 'inicio/cargar_laptop.html', {'formulario': formulario})

def eliminar_laptop(request, laptop_id):
    laptop_a_eliminar = Laptops.objects.get(id=laptop_id)
    laptop_a_eliminar.delete()
    return redirect('laptops') 

def editar_laptop(request, laptop_id):
    laptop_a_editar = Laptops.objects.get(id=laptop_id)
    
    if request.method == "POST":
        formulario = FormularioEditarLaptop(request.POST)
        if formulario.is_valid():
            
            nuevos_atributos = formulario.cleaned_data
            
            laptop_a_editar.marca = nuevos_atributos.get('marca') 
            laptop_a_editar.procesador = nuevos_atributos.get('procesador')
            laptop_a_editar.pulgadas = nuevos_atributos.get('pulgadas')
            laptop_a_editar.save()
            return redirect('laptops')
        else:
            return render(request, 'inicio/editar_laptop.html', {'formulario': formulario})
    
    formulario = FormularioEditarLaptop(initial={'marca':laptop_a_editar.marca.upper(), 'procesador':laptop_a_editar.procesador, 'pulgadas':laptop_a_editar.pulgadas})
    return render(request,'inicio/editar_laptop.html', {'formulario': formulario}) 

def detalle_laptop(request, laptop_id):
    laptop = Laptops.objects.get(id=laptop_id)
    return render(request, 'inicio/detalle_laptop.html', {'laptop': laptop})