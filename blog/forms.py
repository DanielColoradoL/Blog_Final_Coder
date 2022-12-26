from django import forms
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import *

# from django.contrib.auth.forms import  UserCreationForm
# from django.contrib.auth.models import User

# class Form_Post(forms.Form):
#     titulo = forms.CharField(max_length=255)
#     subtitulo = forms.CharField(max_length=255)
#     imagen = forms.ImageField(label="Imagen")
#     cuerpo = RichTextUploadingField() # CKEditor Rich Text Field

class Form_Post(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

    

# null = True. Means there is no constraint of database for the field to be filled, so you can have an object with null value for the filled that has this option. 
# blank = True. Means there is no constraint of validation in django forms.