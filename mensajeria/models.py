from django.db import models
from django.conf import settings
from datetime import datetime

 
# Create your models here.
user = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models


class Mensaje(models.Model):
    enviar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recibir = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    mensaje = models.TextField(max_length=5000)
    a_quehora = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return  str(self.leido) + " "+ self.mensaje + " "+ str(self.a_quehora)

    

