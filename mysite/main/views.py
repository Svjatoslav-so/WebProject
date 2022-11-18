from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Avg
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationUserForm, LoginUserForm, EditProfile
from .models import Product
from blog.models import Post


def if_user_auth_else_login(func):
    def check(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')

    return check


def index(request):
    featured_products = Product.objects.exclude(status="A").annotate(average_rating=Avg('review__rating')).order_by(
        '-average_rating')[:8]
    new_products = Product.objects.exclude(status="A").order_by('-date_of_creation')[:8]

    new_posts = Post.objects.order_by('-date_of_creation')[:2]

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
        "new_posts": new_posts,
    }
    return render(request, "main/index-2.html", context=context)


def contact(request):
    return render(request, "main/contact.html")


def about(request):
    return render(request, "main/about.html")


@if_user_auth_else_login
def account(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print("SAVE")
            print(form)
            # return redirect('index')
        else:
            print(form.errors)
    else:
        form = EditProfile(instance=request.user)
        print("EMPTY")
    context = {
        'form': form
    }
    return render(request, "main/account.html", context=context)


# @if_user_auth_else_login
# def edit_account(request):
#     return render(request, "main/account.html")


def blog(request):
    return render(request, "main/blog.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('account')


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
        "related_products": Product.objects.filter(product_category__slug=cat_slug)[:4]
    }
    return render(request, "main/shop-single-product-2.html", context=context)


class Registration(CreateView):
    form_class = RegistrationUserForm
    template_name = "main/registration.html"
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LogoutUser(LogoutView):
    next_page = reverse_lazy('index')
