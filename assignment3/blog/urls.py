# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL for viewing a single post
    path('post/create/', views.post_create, name='post_create'),  # URL for creating a new post
    path('posts/', views.post_list, name='post_list'),
]
