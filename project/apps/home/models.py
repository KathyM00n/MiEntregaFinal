from django.db import models

# Create your models here.
class Post(models.Model):
    título = models.CharField(max_length=255,)
    contenido = models.TextField()

    def __str__(self):
        return self.título

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    