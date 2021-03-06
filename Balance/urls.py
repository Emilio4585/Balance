"""Balance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('Apps.pages.urls'), name='pages_url'),
    path('posts/', include('Apps.posts.urls'), name='posts_url'),
    path('blogs/', include('Apps.blogs.urls'), name='blogs_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('Apps.accounts.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # add this for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # add this for media
