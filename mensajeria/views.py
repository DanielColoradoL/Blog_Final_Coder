from django.shortcuts import render
from django.contrib.auth.models import User
from mensajeria.models import *
from mensajeria.forms import *
from django.contrib.auth.decorators import login_required
from usuarios.views import obtenerAvatar

@login_required
def mensajeFormulario(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            paraquien = informacion['receiver']
            textoMensaje = informacion['mensaje']
            mensaje1 = Mensaje(enviar=(usuario), recibir = (paraquien), mensaje=textoMensaje, leido = False)
            mensaje1.save()
            formulario = MensajeForm()
            return render(request, 'mensajeFormulario.html', {"form": formulario, "alerta": "El mensaje ha sido enviado exitosamente!", "avatar": obtenerAvatar(request)} )
        else:
            return render(request, 'home.html', {"alerta": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)} )
    else:
        formulario = MensajeForm()
        return render(request, 'mensajeFormulario.html', {"form": formulario, "avatar": obtenerAvatar(request)} )


@login_required
def leerMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(recibir = usuario)
    for mensaje in herram:
        mensaje.leido = True
        mensaje.save()  
    return render(request, "leerMensaje.html", {"mensajes": herram, "avatar": obtenerAvatar(request)})


@login_required
def enviadoMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(enviar = usuario)
    return render(request, "enviadoMensaje.html", {"mensajes": herram, "avatar": obtenerAvatar(request)})


@login_required
def mensajeUsuarios(request):
    return render(request, 'mensajeUsuarios.html',{'users': User.objects.exclude(username=request.user.username), "avatar": obtenerAvatar(request)})