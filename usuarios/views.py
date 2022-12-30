from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.forms import *
from usuarios.models import *
from usuarios.forms import *

def obtenerAvatar(request):
    if request.user.is_authenticated:
        lista = Perfil.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen = lista[0].avatar.url
        else:
            imagen = ""
    else:
        imagen = ""
    return imagen


def register(request):
    if request.method == "POST":
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            usuario = registro.cleaned_data.get("username")
            registro.save()     # Al ser una clase de django, se puede guardar obviando crear un objeto manual
            return render(request, "utilidad.html", {"mensaje_utilidad": f"El usuario {usuario} ha sido creado exitosamente!"})
        else:
           return render(request, "registro.html", {"form_registro" : RegistroForm(), "mensaje_registro": "Intentelo Nuevamente, hubo un error"}) 
    else:
        return render(request, "registro.html", {"form_registro":RegistroForm(), "mensaje_registro":"Registrar usuario", "avatar": obtenerAvatar(request)})


def user_login(request):
    if request.method == "POST":
        credenciales = AuthenticationForm(request, data = request.POST)
        if credenciales.is_valid():
            usuario = credenciales.cleaned_data.get("username")
            clave = credenciales.cleaned_data.get("password")
            log_user = authenticate(username = usuario, password = clave)
            if log_user is not None:
                login(request, log_user)
                return render(request, "utilidad.html", {"mensaje_utilidad": f"Bienvenid@ {usuario} ha iniciado sesion exitosamente!", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "login.html", {"mensaje_login":"Usuario o contraseña incorrectos", "form_login": AuthenticationForm, "avatar": obtenerAvatar(request)})
        else:
            return render(request, "login.html", {"mensaje_login":"Usuario o contraseña incorrectos", "form_login": AuthenticationForm, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "login.html", {"mensaje_login":"Bienvenido de nuevo", "form_login": AuthenticationForm, "avatar": obtenerAvatar(request)})

@ login_required
def user_logout(request):
    logout(request)
    return render(request, "utilidad.html", {"mensaje_utilidad": "Ha cerrado sesion exitosamente!", "avatar": obtenerAvatar(request)})


@ login_required
def user_profile(request):
    datos_perfil = Perfil.objects.filter(user = request.user)
    if datos_perfil:
        descripcion = datos_perfil[0].descripcion
        web = datos_perfil[0].web
    else:
        descripcion = ""
        web = ""
    return render(request, "user_profile.html", {"user" : request.user, "descripcion" : descripcion, "web": web, "avatar": obtenerAvatar(request)})

@ login_required
def user_edit(request):
    if request.method == "POST":
        edit_form = EditUserForm(request.POST, instance = request.user)
        if edit_form.is_valid():
            edit_form.save()
            return render(request, "utilidad.html", {"mensaje_utilidad": f"El usuario {request.user} ha sido editado exitosamente!", "avatar": obtenerAvatar(request)})
        else:
           return render(request, "user_edit.html", {"form_edit_user" : EditUserForm(instance = request.user), "mensaje_registro": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)}) 
    else:
        return render(request, "user_edit.html", {"form_edit_user":EditUserForm(instance = request.user), "mensaje_registro":"Editar perfil", "avatar": obtenerAvatar(request)})

@ login_required
def password_edit(request):
    if request.method == "POST":
        formulario = PasswordChangeForm(data = request.POST, user = request.user)
        if formulario.is_valid():
            formulario.save()
            update_session_auth_hash(request, formulario.user)
            return render(request, "utilidad.html", {"mensaje_utilidad": f"La contraseña ha sido editada exitosamente!", "avatar": obtenerAvatar(request)})
        else:
           return render(request, "password_edit.html", {"form_edit_user" : PasswordChangeForm(user = request.user), "mensaje_registro": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)})
    else:
        return render(request, "password_edit.html", {"form_edit_user": PasswordChangeForm(user = request.user), "mensaje_registro":"Editar contraseña", "avatar": obtenerAvatar(request)})

@ login_required
def profile_edit(request):
    datos_viejos = Perfil.objects.filter(user = request.user)
    if datos_viejos:
        formulario_edit = Form_Perfil(initial={"descripcion": datos_viejos[0].descripcion, "web": datos_viejos[0].web, "avatar": datos_viejos[0].avatar})
    else:
        formulario_edit = Form_Perfil()
    if request.method == "POST":
        formulario = Form_Perfil(request.POST, request.FILES)
        if formulario.is_valid():
            datos_viejos = Perfil.objects.filter(user = request.user)
            if datos_viejos != None:        # Si existe, lo elimina primero para evitar multiples entradas
                datos_viejos.delete()
            datos_nuevos = Perfil(user=request.user, descripcion = request.POST["descripcion"], web = request.POST["web"], avatar = request.FILES["avatar"] )
            datos_nuevos.save()
            return render(request, "utilidad.html", {"mensaje_utilidad": "El perfil ha sido editado exitosamente!", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "profile_edit.html", {"form_edit_profile" : formulario_edit, "mensaje_registro": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)})
    else:
        return render(request, "profile_edit.html", {"form_edit_profile": formulario_edit, "mensaje_registro":"Editar perfil", "avatar": obtenerAvatar(request)}) 


