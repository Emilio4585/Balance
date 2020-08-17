from _ast import mod

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.base import ModelState


class BlogArticulo(models.Model):

    title = models.CharField(default="No Titulo", blank=None,max_length=400)
    contenido_blog = models.TextField(default="No Contenido", blank=None, max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)