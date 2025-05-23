from django.contrib import admin
from .models import Category


# Register your models here.

#Clean Admin Display
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','created_at','updated_at']
    