from django.shortcuts import render
from blog.models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request):
    post = Post.objects.first()
    context = {
        'post' : post
    }
    return render(request, 'blog/post_detail.html', context)