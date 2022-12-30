from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from mensajeria.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("mensajeFormulario", mensajeFormulario , name = "mensajeFormulario"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),

    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
]