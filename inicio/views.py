from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def inicio(request):
   return render(request, 'inicio/inicio.html', {})


def Moviles(request):
   return render(request, 'inicio/moviles.html', {})


def Televisores(request):
   return render(request, 'inicio/televisores.html', {})


def Laptops(request):
   return render(request, 'inicio/laptops.html', {})