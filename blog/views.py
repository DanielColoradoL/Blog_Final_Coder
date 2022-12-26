from django.shortcuts import render
from blog.models import *
from blog.forms import *
from datetime import date


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
    return render(request, "inicio.html", {"blog_1": blog_1, "blog_2": blog_2, "blog_3": blog_3, "blog_4": blog_4}) 
# Post.objects.none() envia un queryset vacio


def post(request, id):
    lectura_publicacion = Post.objects.get(id = id)
    return render(request, "post.html", {"lectura_publicacion" : lectura_publicacion})

def all_posts(request):
    blogs = Post.objects.all().order_by('-id') # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "publicaciones.html", {"blogs": blogs}) 

def about_me(request):
    return render(request, "about.html")

def add_post(request):
    if request.method == "POST":
        formulario = Form_Post(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nueva_publicacion = Post(titulo = datos["titulo"], subtitulo = datos["subtitulo"], cuerpo = datos["cuerpo"], imagen = datos["imagen"] , autor = "Usuario por definir", fecha = date.today())
            nueva_publicacion.save()
            return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido agregado exitosamente!"})
        else:
            return render(request, "addpost.html", {"form_post" : Form_Post(), "mensaje_publicacion": "Intentelo Nuevamente, hubo un error"})
    else:
        return render(request, "addpost.html", {"form_post" : Form_Post(), "mensaje_publicacion": "Agregar un blog"})


def edit_post(request, id):
    blog_edit = Post.objects.get(id = id)
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

            return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido editado exitosamente!"})
        else:
            formulario_edit = Form_Post(initial={"titulo": blog_edit.titulo, "subtitulo": blog_edit.subtitulo, "cuerpo": blog_edit.cuerpo, "imagen": blog_edit.imagen})
            return render(request, "editpost.html", {"form_post" : formulario_edit, "blog_edit": blog_edit, "mensaje_publicacion": "Intentelo Nuevamente, hubo un error"})
    else:
        formulario_edit = Form_Post(initial={"titulo": blog_edit.titulo, "subtitulo": blog_edit.subtitulo, "cuerpo": blog_edit.cuerpo, "imagen": blog_edit.imagen})
        return render(request, "editpost.html", {"form_post": formulario_edit , "mensaje_publicacion": "Editar un blog", "blog_edit": blog_edit})


# Este lo implementare cuando haya creado la lista de post segun usuarios.
def delete_post(request, id):
    blog_delete = Post.objects.get(id=id)
    blog_delete.delete()
    return render(request, "utilidad.html", {"mensaje_utilidad": "El post ha sido eliminado exitosamente!"})