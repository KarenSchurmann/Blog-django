from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = RichTextUploadingField() 
    imagen = models.ImageField(upload_to='media', blank=True)
    autor = models.CharField(max_length=255)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo