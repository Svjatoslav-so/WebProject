from django.shortcuts import render


# Create your views here.
from .models import Post


def blog(request):
    all_posts = Post.objects.all()
    print("ALL_POSTS ", all_posts)
    context = {'all_posts': all_posts}
    return render(request, "blog/blog.html", context=context)


def post(request, post_slug):
    post_details = Post.objects.get(slug=post_slug)
    context = {
        'post': post_details
    }
    return render(request, "blog/blog-details.html", context=context)
