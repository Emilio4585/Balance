
from django.urls import path
from .views import Home, About


urlpatterns = [
    path('', Home.as_view(), name='home_pages'),
    path('about/', About.as_view(), name='about_pages'),

]

