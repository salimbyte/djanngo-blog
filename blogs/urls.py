from django.urls import path
from .views import *

app_name = 'blogs'



urlpatterns = [
    path('create/', create_blog, name='blog_create'),
    path('delete/<int:pk>', delete_blog, name='blog_delete'),
    path('add/<int:blog_id>', add_comment, name='add_comment'),
]
