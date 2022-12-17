from django.urls import path
from blog.views import *

urlpatterns = [
    path("", inicio, name= "inicio"), 
]