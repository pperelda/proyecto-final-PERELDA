from django.db import models

class Moviles(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    mpx_camara = models.IntegerField()
# AGREGAR OTROS CAMPOS DE INFORMACION --- DATEFIELD/DESCRIPCION, ETC    
    def __str__(self):
        return f'{self.marca.capitalize()} - {self.modelo} - {self.color.capitalize()}'

class Televisores(models.Model):
    marca = models.CharField(max_length=30)
    pulgadas = models.IntegerField()
    definicion = models.TextField()
    es_smart = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.marca.upper()} - {self.pulgadas}"'
    
class Laptops(models.Model):
    marca = models.CharField(max_length=30)
    procesador = models.TextField()
    pulgadas = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca.capitalize()} - {self.procesador} - {self.pulgadas}"'
   