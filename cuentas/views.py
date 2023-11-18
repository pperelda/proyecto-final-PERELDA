from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import FormularioRegistroUsuario, FormularioEditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login(request):    
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=clave) 
            django_login(request, user)
            
            return redirect('inicio')
    
    return render(request, 'cuentas/login.html', {'login_formulario': formulario})

def registro_usuario(request):
    formulario = FormularioRegistroUsuario()
    
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
         
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    return render(request, 'cuentas/registro.html', {'formulario_de_registro': formulario})

def perfil(request):
    return render(request, 'cuentas/perfil.html', {} )

def editar_perfil(request):
    formulario = FormularioEditarPerfil(instance = request.user)
    
    if request.method == 'POST':
        formulario = FormularioEditarPerfil(request.POST, instance = request.user)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class editar_password(PasswordChangeView):
    template_name = 'cuentas/editar_password.html'
    success_url = reverse_lazy('perfil')

