from django import forms
 
class vehiculoFormulario(forms.Form):
    vehiculo = forms.CharField()
    modelo = forms.IntegerField()

class pilotoFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    emial= forms.EmailField()

class carreraFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    fechalimite=forms.BooleanField()
    fechallegada=forms.BooleanField()

