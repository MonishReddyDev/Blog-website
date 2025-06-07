from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.posts_by_category, name='posts_by_category'),
    path('blog/<slug:slug>',views.blog_detail,name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete/<slug:slug>/', views.delete_blog, name='delete_blog'),


]