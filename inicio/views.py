from inicio.forms import FormularioCrearTelevisor, FormularioCrearLaptop
from inicio.forms import FormularioEditarTelevisor, FormularioEditarLaptop
from inicio.models import Moviles, Televisores, Laptops
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio(request):
   return render(request, 'inicio/inicio.html', {})


# ==================== MOVILES, con clases basadas en vistas =====================


class ListadoMoviles(ListView): 
    model = Moviles
    context_object_name = 'listado_moviles'
    template_name = 'inicio/moviles.html'

class cargar_movil(LoginRequiredMixin, CreateView):
    model = Moviles
    template_name = 'inicio/cargar_movil.html'
    fields = ['marca', 'modelo', 'color', 'mpx_camara', 'imagen']
    success_url = reverse_lazy('moviles') 
    
class eliminar_movil(LoginRequiredMixin, DeleteView):
    model = Moviles 
    template_name = 'inicio/eliminar_movil.html'
    success_url = reverse_lazy('moviles')  
    
class editar_movil(LoginRequiredMixin, UpdateView):
    model = Moviles
    template_name = 'inicio/editar_movil.html'
    fields = ['marca', 'modelo', 'color', 'mpx_camara', 'imagen']
    success_url = reverse_lazy('moviles')   

class detalle_movil(DetailView):
    model = Moviles
    template_name = 'inicio/detalle_movil.html'
    
    
# ==================== TELEVISORES =====================

def Televisores_principal(request):
    
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_televisores = Televisores.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_televisores = Televisores.objects.all()
     
    return render(request, 'inicio/televisores.html', {'listado_televisores':listado_televisores,'marca_a_buscar':marca_a_buscar})

@login_required
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

@login_required
def eliminar_televisor(request, televisor_id):
    televisor_a_eliminar = Televisores.objects.get(id=televisor_id)
    televisor_a_eliminar.delete()
    return redirect('televisores') 

@login_required
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
    return render(request, 'inicio/laptops.html', {'listado_laptops': listado_laptops, 'marca_a_buscar':marca_a_buscar })

@login_required
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

@login_required
def eliminar_laptop(request, laptop_id):
    laptop_a_eliminar = Laptops.objects.get(id=laptop_id)
    laptop_a_eliminar.delete()
    return redirect('laptops') 

@login_required
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