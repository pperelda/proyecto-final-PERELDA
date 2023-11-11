from django.contrib import admin
from inicio.models import Moviles, Televisores, Laptops

admin.site.register([Moviles, Televisores, Laptops])
