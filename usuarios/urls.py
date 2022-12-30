from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("login", user_login, name= "login"), 
    path("register", register, name= "register"), 
    path("logout", user_logout, name= "logout"),
    path("userprofile", user_profile, name= "user_profile"),
    path("useredit", user_edit, name= "user_edit"), 
    path("passwordedit", password_edit, name= "password_edit"),
    path("profileedit", profile_edit, name= "profile_edit"),
]