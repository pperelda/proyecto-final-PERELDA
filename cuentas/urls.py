from django.urls import path
from cuentas.views import login, registro_usuario, perfil, editar_perfil, editar_password, contacto
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login, name='login'),
    path('logout/', LogoutView.as_view(template_name= 'cuentas/logout.html'), name='logout'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('perfil/', perfil, name='perfil'),
    path('editar/perfil/', editar_perfil, name='editar_perfil'),
    path('editar/password/', editar_password.as_view(), name='editar_password'),
    path('contacto', contacto, name='contacto')
]
