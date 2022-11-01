from django.shortcuts import render


# Create your views here.
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
