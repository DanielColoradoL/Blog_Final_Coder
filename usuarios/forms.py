from django import forms
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import *

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Ingrese nombre")
    last_name = forms.CharField(label="Ingrese apellido")
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        help_texts = {x:"" for x in fields} #para cada uno de los campos del formulario, le asigna un valor vacio


class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        help_texts = {x:"" for x in fields} #para cada uno de los campos del formulario, le asigna un valor vacio


class Form_Perfil(ModelForm):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'web', 'avatar']
