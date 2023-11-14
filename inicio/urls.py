from django.urls import path
from inicio.views import inicio, Moviles_principal, Televisores_principal, Laptops_principal 
from inicio.views import cargar_movil, cargar_televisor, cargar_laptop
from inicio.views import eliminar_movil, eliminar_televisor, eliminar_laptop
from inicio.views import editar_movil, editar_televisor, editar_laptop
from inicio.views import detalle_movil, detalle_televisor, detalle_laptop

urlpatterns = [
    path('', inicio, name= 'inicio'),
    
    path('moviles', Moviles_principal, name='moviles'),
    path('moviles/cargar/', cargar_movil, name='cargar_movil'),
    path('moviles/<int:movil_id>/eliminar/', eliminar_movil, name='eliminar_movil'),
    path('moviles/<int:movil_id>/editar/', editar_movil, name='editar_movil'),
    path('moviles/<int:movil_id>/detalle/', detalle_movil, name='detalle_movil'),
    
    
    
    path('televisores', Televisores_principal, name='televisores'),
    path('televisores/cargar/', cargar_televisor, name='cargar_televisor'),
    path('televisores/<int:televisor_id>/eliminar/', eliminar_televisor, name='eliminar_televisor'),
    path('televisores/<int:televisor_id>/editar/', editar_televisor, name='editar_televisor'),
    path('televisores/<int:televisor_id>/detalle/', detalle_televisor, name='detalle_televisor'),
    
    
    
    path('laptops', Laptops_principal, name='laptops'),
    path('laptops/cargar/', cargar_laptop, name='cargar_laptop'),
    path('laptops/<int:laptop_id>/eliminar/', eliminar_laptop, name='eliminar_laptop'),
    path('laptops/<int:laptop_id>/editar/', editar_laptop, name='editar_laptop'),
    path('laptops/<int:laptop_id>/detalle/', detalle_laptop, name='detalle_laptop'),        
]
