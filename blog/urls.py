from django.urls import path
from blog.views import *

urlpatterns = [
    path("", inicio, name= "inicio"), 
    path("post/<id>", post, name = "post"),
    path("about", about_me, name= "about_me"),
    path("allposts", all_posts, name= "all_posts"),
    path("addpost", add_post, name= "add_post"),
    path("editpost/<id>", edit_post, name= "edit_post"),
    path("bitacora", bitacora, name= "bitacora"),
    path("delete/<id>", delete_post, name= "delete"),
    path("bitacoraadmin", bitacora_admin, name= "bitacora_admin"),
]