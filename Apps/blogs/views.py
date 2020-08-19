from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostBlog
from django.urls import reverse_lazy, reverse


# Create your views here.


class BlogListView(ListView):
    model = PostBlog
    template_name = 'blog/blog_main.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = PostBlog
    template_name = 'blog/blog_detail.html'
    context_object_name = "detail_blog"


class BlogCreateView(CreateView):
    model = PostBlog
    template_name = 'blog/blog_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = PostBlog
    template_name = 'blog/blog_edit.html'
    fields = '__all__'


class BlogDeleteView(DeleteView):
    model = PostBlog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blogs_home')
