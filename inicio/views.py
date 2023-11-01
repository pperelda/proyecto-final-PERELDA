from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from inicio.forms import formulario_moviles


def inicio(request):
   return render(request, 'inicio/inicio.html', {})


def Moviles(request):
    # if request.method == 'POST':    
    #     marca= request.POST.get('marca')
    #     modelo= request.POST.get('modelo')
    #     color= request.POST.get('color')
    #     mpx_camara= request.POST.get('mpx_camara')
        
    #     movil = Moviles(marca=marca, modelo=modelo, color=color, mpx_camara=mpx_camara)
    #     movil.save()
    
    if request.method == 'POST': 
        
    formulario = formulario_moviles()
    return render(request, 'inicio/moviles.html', {'formulario': formulario})


def Televisores(request):
   return render(request, 'inicio/televisores.html', {})


def Laptops(request):
   return render(request, 'inicio/laptops.html', {})