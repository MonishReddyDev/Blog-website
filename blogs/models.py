from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'