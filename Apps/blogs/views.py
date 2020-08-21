from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostBlog
from django.urls import reverse_lazy


# Create your views here.


class BlogListView(ListView):
    """Lista todos los blogs """
    model = PostBlog
    template_name = 'blog/blog_main.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    """Muestra el detalle de cada blog"""
    model = PostBlog
    template_name = 'blog/blog_detail.html'
    context_object_name = "detail_blog"


class BlogCreateView(CreateView):
    """Crea un nuevo blog"""
    model = PostBlog
    template_name = 'blog/blog_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    """Edita un existente blog"""
    model = PostBlog
    template_name = 'blog/blog_edit.html'
    fields = '__all__'


class BlogDeleteView(DeleteView):
    """Elimina un blog de la base de datos"""
    model = PostBlog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blogs_home')


class BlogLogin(LoginView):
    """Muestra un login de el usuario"""
    template_name = 'blog/registration/login.html'


class BlogLogout(LogoutView):
    template_name = 'blog/registration/logout.html'
