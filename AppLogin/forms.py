from django import forms

#Cada vez que se intancie esta clase se creara un formulario con estos campos
class FormularioLogin(forms.Form):
    usuario=forms.CharField()
    contrasena= forms.CharField(widget=forms.PasswordInput, label="Contraseña")