from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import FormularioRegistroUsuario, FormularioEditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.models import DatosExtra
from django.core.mail import send_mail
from django.conf import settings


def login(request):    
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=clave) 
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
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
    
    datos_extra = request.user.datosextra   #'datosextra' se forma a partir de DatosExtra TODO EN MINUSCULA
    formulario = FormularioEditarPerfil(initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar}, instance = request.user)
    
    if request.method == 'POST':        
        formulario = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
            datos_extra.save()
            formulario.save()
            
            return redirect('perfil')
        
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class editar_password(PasswordChangeView):
    template_name = 'cuentas/editar_password.html'
    success_url = reverse_lazy('perfil')


def contacto(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = 'Remitente: '+ request.POST['email']+ '\n' + request.POST['mensaje']  
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['pabloperelda@gmail.com']
        
        send_mail(asunto, mensaje, email_from, recipient_list)
   
        return redirect('inicio')
    return render(request, 'cuentas/contacto.html')

def about_us(request):
    return render(request, 'cuentas/about_us.html')