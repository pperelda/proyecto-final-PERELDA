from django.urls import path
from inicio.views import inicio, Moviles, Televisores, Laptops 
from inicio.views import cargar_movil, cargar_televisor, cargar_laptop 

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('moviles', Moviles, name='moviles'),
    path('televisores', Televisores, name='televisores'),
    path('laptops', Laptops, name='laptops'),
    path('moviles/cargar/', cargar_movil, name='cargar_movil'),
    path('televisores/cargar/', cargar_televisor, name='cargar_televisor'),
    path('laptops/cargar/', cargar_laptop, name='cargar_laptop')        
]
