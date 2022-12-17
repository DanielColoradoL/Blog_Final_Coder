from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# class Post(models.Model):

#     title = models.CharField(max_length=255)
#     #body = models.TextField() 
#     body = RichTextUploadingField() # CKEditor Rich Text Field

#     def __str__(self):
#         return self.title