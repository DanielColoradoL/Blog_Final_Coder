from django.shortcuts import render
from blog.models import *

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
    return render(request, "index.html", {"blog_1": blog_1, "blog_2": blog_2, "blog_3": blog_3, "blog_4": blog_4})


# Post.objects.none() envia un queryset vacio