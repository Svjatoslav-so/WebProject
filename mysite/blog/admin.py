from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Tag, Post, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    fields = ('id', 'title', 'slug')
    readonly_fields = ('id',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_html_photo', 'date_of_creation')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'author', 'id')
    fields = ('id', 'title', 'slug', 'author', 'get_html_photo', 'photo', 'text', 'tags', 'date_of_creation',
              'edit_date', 'comments')
    readonly_fields = ('id', 'get_html_photo', 'comments', 'date_of_creation', 'edit_date')
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=50>")

    get_html_photo.short_description = "Фото"


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'date_of_creation')
    list_display_links = ('id', 'post')
    search_fields = ('post', 'user', 'text', 'id')
    fields = ('id', 'text', 'date_of_creation', 'edit_date', 'post', 'user')
    readonly_fields = ('id',)


admin.site.register(Comment, CommentAdmin)
