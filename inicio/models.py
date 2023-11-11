from django.db import models

class Moviles(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.TextField()
    color = models.CharField(max_length=15)
    mpx_camara = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.color} - {self.mpx_camara}mpx'

class Televisores(models.Model):
    marca = models.CharField(max_length=30)
    pulgadas = models.IntegerField()
    definicion = models.TextField()
    es_smart = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.pulgadas}" - {self.definicion}'
    
class Laptops(models.Model):
    marca = models.CharField(max_length=30)
    procesador = models.TextField()
    pulgadas = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.procesador} - {self.pulgadas}"'
   