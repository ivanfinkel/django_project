from django import forms

# Create your forms here.

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length= 60)
    apellido = forms.CharField(max_length= 60)
    email = forms.EmailField(max_length=50)
    profesion = forms.CharField(max_length= 60)

class FamiliarFormulario(forms.Form):

    parentesco = forms.CharField(max_length=40)
    nombre = forms.CharField(max_length= 60)
    edad = forms.IntegerField()
    fecha = forms.DateField()