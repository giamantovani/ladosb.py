from django.db import models

# Create your models here.
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

# vinylstore/models.py
from django.db import models

class Disco(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='img/')
    tracklist = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
