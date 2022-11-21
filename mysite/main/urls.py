from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:cat_slug>/<slug:prod_slug>', views.product, name='product'),

]
