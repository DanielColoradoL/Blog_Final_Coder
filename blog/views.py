from django.shortcuts import render
from blog.models import *
from blog.forms import *
from datetime import date
from django.contrib.auth.decorators import login_required
from usuarios.views import obtenerAvatar

def inicio(request):
    blogs = Post.objects.all().order_by('-id')[:4] # Consulta por id, y limita a 4 de mayor a menor (ORDER BY id DESC en SQL) (LIMIT 4)
    if len(blogs) == 0:
        blog_1 = Post.objects.none()
        blog_2 = Post.objects.none()
        blog_3 = Post.objects.none()
        blog_4 = Post.objects.none()
    elif len(blogs) == 1:
        blog_1 = blogs[0]
        blog_2 = Post.objects.none()
        blog_3 = Post.objects.none()
        blog_4 = Post.objects.none()
    elif len(blogs) == 2:
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = Post.objects.none()
        blog_4 = Post.objects.none()
    elif len(blogs) == 3:
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = blogs[2]
        blog_4 = Post.objects.none()
    else:     
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = blogs[2]
        blog_4 = blogs[3]
    return render(request, "inicio.html", {"blog_1": blog_1, "blog_2": blog_2, "blog_3": blog_3, "blog_4": blog_4, "avatar": obtenerAvatar(request)}) 
# Post.objects.none() envia un queryset vacio


def post(request, id):
    lectura_publicacion = Post.objects.get(id = id)
    return render(request, "post.html", {"lectura_publicacion" : lectura_publicacion, "avatar": obtenerAvatar(request)})


def all_posts(request):
    blogs = Post.objects.all().order_by('-id') # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "publicaciones.html", {"blogs": blogs, "avatar": obtenerAvatar(request)}) 


@ login_required
def bitacora(request):
    user_name = request.user.get_full_name()
    blogs = Post.objects.filter(autor = user_name).order_by("-id") # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "bitacora.html", {"blogs": blogs, "avatar": obtenerAvatar(request)}) 


def about_me(request):
    return render(request, "about.html", {"avatar": obtenerAvatar(request)})


@ login_required
def add_post(request):
    if request.method == "POST":
        formulario = Form_Post(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre_autor = request.user.get_full_name()
            nueva_publicacion = Post(titulo = datos["titulo"], subtitulo = datos["subtitulo"], cuerpo = datos["cuerpo"], imagen = datos["imagen"] , autor = nombre_autor, fecha = date.today())
            nueva_publicacion.save()
            return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido agregado exitosamente!"})
        else:
            return render(request, "addpost.html", {"form_post" : Form_Post(), "mensaje_publicacion": "Intentelo Nuevamente, hubo un error"})
    else:
        return render(request, "addpost.html", {"form_post" : Form_Post(), "mensaje_publicacion": "Agregar un blog", "avatar": obtenerAvatar(request)})


@ login_required
def edit_post(request, id):
    user_name = request.user.get_full_name()
    blog_edit = Post.objects.get(id = id)
    if user_name == blog_edit.autor or request.user.is_superuser:        # Este If valida que el usuario que va a editar sea el mismo que publico el blog. Para evitar que los usuarios accedan a los blogs de otros usuarios.
        if request.method == "POST":
            formulario = Form_Post(request.POST, request.FILES)
            if formulario.is_valid():
                datos = formulario.cleaned_data
                # Este if, limpia la imagen cuando se usa el checkbox clear, deja la imagen anterior, si existe, si no no carga nada, y actualiza cuando hay una imagen nueva
                info_imagen = datos["imagen"]
                if str(type(info_imagen)) == "<class 'NoneType'>":      # Si el campo de imagen no tiene cambios, simplemente no actualiza el objeto de la db.
                    pass
                elif str(info_imagen) == "False":                       # Si devuelve False (valor por defecto del checkbox con label clear), que guarde un None osea nada
                    blog_edit.imagen = None
                else:                                                   # Si entra al else, es por que se le cargo una imagen.
                    blog_edit.imagen = datos["imagen"]

                blog_edit.titulo = datos["titulo"]
                blog_edit.subtitulo = datos["subtitulo"]
                blog_edit.cuerpo = datos["cuerpo"]
                blog_edit.save()

                return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido editado exitosamente!", "avatar": obtenerAvatar(request)})
            else:
                formulario_edit = Form_Post(initial={"titulo": blog_edit.titulo, "subtitulo": blog_edit.subtitulo, "cuerpo": blog_edit.cuerpo, "imagen": blog_edit.imagen})
                return render(request, "editpost.html", {"form_post" : formulario_edit, "blog_edit": blog_edit, "mensaje_publicacion": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)})
        else:
            formulario_edit = Form_Post(initial={"titulo": blog_edit.titulo, "subtitulo": blog_edit.subtitulo, "cuerpo": blog_edit.cuerpo, "imagen": blog_edit.imagen})
            return render(request, "editpost.html", {"form_post": formulario_edit , "mensaje_publicacion": "Editar un blog", "blog_edit": blog_edit, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "utilidad.html", {"mensaje_utilidad": "No tiene autorizacion de editar esta publicacion!", "avatar": obtenerAvatar(request)})


@ login_required
def delete_post(request, id):
    user_name = request.user.get_full_name()
    blog_delete = Post.objects.get(id=id)
    if user_name == blog_delete.autor or request.user.is_superuser:      # Este If valida que el usuario que va a eliminar sea el mismo que publico el blog. Para evitar que los usuarios accedan a los blogs de otros usuarios.
        blog_delete.delete()
        return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido eliminado exitosamente!"})
    else:
        return render(request, "utilidad.html", {"mensaje_utilidad": "No tiene autorizacion de eliminar esta publicacion!", "avatar": obtenerAvatar(request)})


@ login_required
def bitacora_admin(request):
    blogs = Post.objects.all().order_by("-id") # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "bitacoraadmin.html", {"blogs": blogs, "avatar": obtenerAvatar(request)}) 