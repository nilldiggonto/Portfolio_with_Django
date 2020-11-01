from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def blog_page(request):
    template_name = 'blog/blog.html'
    blogs = Blog.objects.all
    context = {
        'blogs':blogs
    }
    return render(request,template_name,context )


def blog_detail(request,id):
    template_name = 'blog/detail.html'

    blog_detail =get_object_or_404(Blog,pk=id)
    context = {
        'blog':blog_detail, 
    }
    return render(request,template_name,context)