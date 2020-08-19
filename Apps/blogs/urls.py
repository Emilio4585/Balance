from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs_home'),
    path('create/', BlogCreateView.as_view(), name='blog_new'), #Create        C
    path('read/<pk>', BlogDetailView.as_view(), name='blog_view'), #Read       R
    path('update/<pk>', BlogUpdateView.as_view(), name='blog_edit'), #Update   U
    path('delete/<pk>', BlogDeleteView.as_view(), name='blog_delete'), #Update D
]
