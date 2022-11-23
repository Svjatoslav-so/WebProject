from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
from .models import Post


def blog(request):
    if request.method == 'GET':
        tag = request.GET.get('tag')
        if tag:
            all_posts = Post.objects.filter(tags__slug=tag)
        else:
            all_posts = Post.objects.all()
    else:
        all_posts = Post.objects.all()
    print("ALL_POSTS ", all_posts)

    paginator = Paginator(all_posts, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {'page_obj': page_obj}
    return render(request, "blog/blog.html", context=context)


def post(request, post_slug):
    post_details = Post.objects.get(slug=post_slug)
    context = {
        'post': post_details
    }
    return render(request, "blog/blog-details.html", context=context)
