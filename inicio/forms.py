from django import forms 

 # ========== Moviles =============
class FormularioBaseMovil(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=15)
    mpx_camara = forms.IntegerField()

class FormularioCrearMovil(FormularioBaseMovil):
    ...

class FormularioEditarMovil(FormularioBaseMovil):
    ...
 
 # ========== Televisores =============
class FormularioBaseTelevisor(forms.Form):
    marca = forms.CharField(max_length=30)
    pulgadas = forms.IntegerField()
    definicion = forms.CharField(max_length=15)
    es_smart = forms.CharField(max_length=2) 

class FormularioCrearTelevisor(FormularioBaseTelevisor):
    ...
    
class FormularioEditarTelevisor(FormularioBaseTelevisor):
    ...

#============== Laptops =============
class FormularioBaseLaptop(forms.Form):
    marca = forms.CharField(max_length=30)
    procesador = forms.CharField(max_length=15)
    pulgadas = forms.IntegerField()

class FormularioCrearLaptop(FormularioBaseLaptop):
    ...
    
class FormularioEditarLaptop(FormularioBaseLaptop):
    ...