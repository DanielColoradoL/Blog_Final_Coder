from django.urls import path
from blog.views import *

urlpatterns = [
    path("", inicio, name= "inicio"), 
    path("post/<id>", post, name = "post"),
    path("about", about_me, name= "about_me"),
    path("allposts", all_posts, name= "all_posts"),
]