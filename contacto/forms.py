from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(max_length=100, label="Nombre", required=True)
    email=forms.CharField(max_length=100, label="Email", required=True)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)