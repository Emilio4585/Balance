from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import PostBlog


# Create your views here.


class HomeListView(ListView):
    model = PostBlog
    template_name = 'blog/main.html'
    context_object_name = 'blogs'
    paginate_by = 2


class HomeView(DetailView):
    model = PostBlog
    template_name = 'blog/blog_detail.html'
    context_object_name = "detail_blog"
