from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Blog,Category,Comment
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect
from .forms import BlogForm

@login_required
def create_blog(request):
    if request.method == 'POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog =form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm()
    return render(request,'blogs/create_blog.html',{'form': form})

@login_required
def edit_blog(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    
    if(blog.author != request.user):
         return HttpResponseForbidden("You are not allowed to edit this blog.")
     
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form=BlogForm(instance=blog)
    
    return render(request, 'blogs/edit_blog.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request,slug):
    blog =get_object_or_404(Blog,slug=slug)
    
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog.")
    if request.method=='POST':
        blog.delete()
        return redirect('home')
    return render(request,'blogs/delete_blog_confirm.html',{'blog':blog})

    

# Create your views here.
def home(request):
    query = request.GET.get('q')
    
    if query:
        featured_blogs=Blog.objects.filter(title__icontains=query,status='public')
        recent_blogs=Blog.objects.filter(title__icontains=query,status='public')
    else:
        featured_blogs = Blog.objects.filter(status='public', is_featured=True).order_by('-created_at')[:3]
        recent_blogs = Blog.objects.filter(status='public', is_featured=False).order_by('-created_at')[:6]

    categories=Category.objects.all()
    
    return render(request, 'blogs/home.html', {
        'categories': categories,
        'featured_blogs': featured_blogs,
        'recent_blogs': recent_blogs,
        'query': query
    })
    

def posts_by_category(request , slug):
    category= get_object_or_404(Category, id=slug)
    blogs =Blog.objects.filter(category=category,status='public').order_by('-created_at')
    categories= Category.objects.all()
    print(categories)
    return render(request, 'blogs/posts_by_category.html', {
        'category': category,
        'blogs': blogs,
        'categories': categories
    })
    

def blog_detail(request,slug):
    blog=get_object_or_404(Blog,slug=slug,status='public')
    comments = blog.comments.all().order_by('-created_at') # type: ignore
    categories=Category.objects.all()
    
    if request.method =='POST':
        comment_text=request.POST.get('comment')
        if request.user.is_authenticated and comment_text:
            Comment.objects.create(blog=blog ,user=request.user,comment=comment_text)
            return HttpResponseRedirect(reverse('blog_detail',args=[slug]))
    
    return  render(request,'blogs/blog_detail.html',{
        'blog': blog,
        'comments':comments,
        'categories': categories
    })


