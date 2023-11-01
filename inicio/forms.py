from django import forms 

class FormularioCrearMovil(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=15)
    mpx_camara = forms.IntegerField()
    
class FormularioCrearTelevisores(forms.Form):
    marca = forms.CharField(max_length=30)
    pulgadas = forms.IntegerField()
    definicion = forms.CharField(max_length=15)
    es_smart = forms.CharField(max_length=2)
    
class FormularioCrearLaptops(forms.Form):
    marca = forms.CharField(max_length=30)
    procesador = forms.CharField(max_length=15)
    pulgadas = forms.IntegerField()
    