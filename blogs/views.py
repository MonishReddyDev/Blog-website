from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.filter(category__category_name='Technology').order_by('-created_at')
    print(blogs)
    return render(request, 'blogs/home.html', {'blogs': blogs})

    
