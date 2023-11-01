from django.db import models

class Moviles(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.TextField()
    color = models.CharField(max_length=15)
    mp_camara_frontal = models.IntegerField()

class Televisores(models.Model):
    marca = models.CharField(max_length=30)
    pulgadas = models.IntegerField()
    definicion = models.TextField()
    es_smart = models.CharField(max_length=30)
    
class Laptops(models.Model):
    marca = models.CharField(max_length=30)
    procesador = models.TextField()
    pulgadas = models.IntegerField()
    descripcion = models.TextField()