from django.urls import path
from inicio.views import inicio, Moviles, Televisores, Laptops, cargar_movil 

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('moviles', Moviles, name='moviles'),
    path('televisores', Televisores, name='televisores'),
    path('laptops', Laptops, name='laptops'),
    path('moviles/cargar/', cargar_movil, name='cargar_movil'),        
]
