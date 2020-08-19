from django.urls import path
from .views import HomeListView, HomeView

urlpatterns = [
    path('', HomeListView.as_view(), name='home_blogs'),
    path('aut/<pk>', HomeView.as_view(), name='blog_view')
]
