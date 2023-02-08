from django.db import models

# Create your models here.

class Curso (models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()


class Profesor(models.Model):

    nombre = models.CharField(max_length= 60)
    apellido = models.CharField(max_length= 60)
    email = models.EmailField(max_length=50)
    profesion = models.CharField(max_length= 60)

class Familiar(models.Model):

    parentesco = models.CharField(max_length=40)
    nombre = models.CharField(max_length= 60)
    edad = models.IntegerField()
    fecha = models.DateField()

