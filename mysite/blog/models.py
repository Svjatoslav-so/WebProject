from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=55, unique=True, verbose_name="Тег")

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Пост")
    photo = models.ImageField(upload_to="photos/post/%Y/%m/%d/", verbose_name="Фото")
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Теги")
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания поста")
    edit_date = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования")
    comments = models.ManyToManyField(User, through='Comment', verbose_name='Комментарии', blank=True,
                                      related_name='comment_user')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['date_of_creation']

    def __str__(self):
        return f"id({self.pk}) {self.title} - {self.author}"


class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания комментария")
    edit_date = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
