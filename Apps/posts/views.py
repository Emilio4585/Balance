from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post


# Create your views here.


class Home(ListView):
    model = Post
    template_name = "posts/main.html"
    context_object_name = "posts"
