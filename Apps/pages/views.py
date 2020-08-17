from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'pages/main.html'

class About(TemplateView):
    template_name = 'pages/about.html'