from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Avg
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Product


def index(request):
    featured_products = Product.objects.exclude(status="A").annotate(average_rating=Avg('review__rating')).order_by(
        '-average_rating')[:8]
    new_products = Product.objects.exclude(status="A").order_by('date_of_creation')[:8]
    for r in featured_products:
        print(r, r.average_rating)
    context = {"main_slides": [
        ("1.jpg", "Лодочки"),
        ("2.jpg", "Катера"),
        ("3.jpg", "Яхты"),
        ("4.jpg", "Гоночные яхты"),
        ("5.jpg", "Принимайте участие в соревнованиях"),
        ("6.jpg", "Получайте удовольствие")
    ],
        "featured_products": featured_products,
        "new_products": new_products,
    }
    return render(request, "main/index-2.html", context=context)


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
    context = {
        'goods': goods
    }
    return render(request, "main/shop.html", context=context)


def product(request, cat_slug, prod_slug):
    try:
        prod = Product.objects.filter(slug=prod_slug).annotate(review_count=Count('reviews')).get()
    except ObjectDoesNotExist:
        return redirect("shop")

    context = {
        "product": prod,
        "related_products": Product.objects.filter(product_category=prod.product_category)[:4]
    }
    return render(request, "main/shop-single-product-2.html", context=context)
