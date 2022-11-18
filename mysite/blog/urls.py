from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post_slug>/', views.post, name='post'),
]
