from django import forms 

class formulario_moviles(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.TextInput()
    color = forms.CharField(max_length=15)
    mpx_camara = forms.IntegerField()