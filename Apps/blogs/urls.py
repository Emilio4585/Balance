from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogLogin,
    BlogLogout,
)
urlpatterns = [
    path('', BlogListView.as_view(), name='blogs_home'),
    path('create/', BlogCreateView.as_view(), name='blog_new'), #Create        C
    path('read/<pk>', BlogDetailView.as_view(), name='blog_view'), #Read       R
    path('update/<pk>', BlogUpdateView.as_view(), name='blog_edit'), #Update   U
    path('delete/<pk>', BlogDeleteView.as_view(), name='blog_delete'), #Update D
    path('login/', BlogLogin.as_view(), name='blog_login'),
    path('logout/', BlogLogout.as_view(), name='blog_logout'),
]
