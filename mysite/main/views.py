from django.shortcuts import render

# Create your views here.
from .models import Product


def index(request):
    return render(request, "main/index-2.html")


def contact(request):
    return render(request, "main/contact.html")


def about(request):
    return render(request, "main/about.html")


def account(request):
    return render(request, "main/account.html")


def blog(request):
    return render(request, "main/blog.html")


def login(request):
    return render(request, "main/login.html")


def wishlist(request):
    return render(request, "main/shop-wishlist.html")


def shop(request):
    goods = Product.objects.all()
    gp = []
    for g in goods:
        p = g.productphoto_set.all()[0]
        print(p)
        gp.append((g, p))
    context = {
        'goods': gp
    }
    return render(request, "main/shop.html", context=context)
