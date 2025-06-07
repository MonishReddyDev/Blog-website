from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title', 'slug', 'category', 'blog_image',
            'short_description', 'blog_body', 'status', 'is_featured'
        ]