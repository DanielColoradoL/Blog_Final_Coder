from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    descripcion = models.CharField(max_length=255)
    web =  models.URLField(max_length=200)
    avatar = models.ImageField(upload_to='avatar')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.avatar}"