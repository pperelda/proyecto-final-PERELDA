from django.urls import path
from inicio.views import inicio, Moviles_principal, Televisores_principal, Laptops_principal 
from inicio.views import cargar_movil, cargar_televisor, cargar_laptop 

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('moviles', Moviles_principal, name='moviles'),
    path('televisores', Televisores_principal, name='televisores'),
    path('laptops', Laptops_principal, name='laptops'),
    path('moviles/cargar/', cargar_movil, name='cargar_movil'),
    path('televisores/cargar/', cargar_televisor, name='cargar_televisor'),
    path('laptops/cargar/', cargar_laptop, name='cargar_laptop')        
]
