from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default=None, blank=True, verbose_name='Nombre')
    apellidoPaterno = models.CharField(max_length=30, default=None, blank=True, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=30, default=None, blank=True, verbose_name='Apellido Materno')
    edad = models.IntegerField(verbose_name='Edad')
