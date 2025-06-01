from django.contrib import admin
from .models import Category,Blog


# Register your models here.

#Clean Admin Display
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','created_at','updated_at']


# category__category_name tells Django:
# "Search through the category field and match against the category_name inside it"

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category','blog_image', 'author', 'status', 'is_featured', 'created_at','updated_at']
    list_filter = ['status', 'is_featured', 'created_at']
    search_fields = ['title', 'short_description', 'blog_body','category__category_name']
    list_editable=('is_featured',)
    prepopulated_fields={'slug':('title',)}
    ordering = ['-created_at']
    
