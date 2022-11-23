from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import ProductPhoto, Product, Material, Manufacturer, Category, Review

admin.site.site_title = 'Yacht RC'
admin.site.site_header = 'Админ-панель Yacht RC'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount', 'manufacturer', 'status', 'amount')
    list_display_links = ('id', 'title')
    search_fields = ('product_code', 'title', 'slug')
    fields = (('id', 'product_code'),
              'slug',
              ('title', 'price'),
              'discount',
              'status',
              'get_html_photos',
              ('warranty_period', 'return_period'),
              'amount',
              'product_category',
              'description',
              'manufacturer',
              'material',
              'model_power_supply',
              'r_controller_power_supply',
              'engine_type',
              'channel_frequency',
              'num_of_channels',
              'camera_presence',
              'kit_type',
              'length',
              'height',
              'width',
              'complete_set',
              'packing_size',
              'feature',
              'date_of_creation',
              'reviews',
              )

    prepopulated_fields = {'slug': ('title', 'product_code')}
    readonly_fields = ('id', 'get_html_photos', 'date_of_creation', 'reviews')

    def get_html_photos(self, obj):
        photos_html = ''
        for p in ProductPhoto.objects.filter(product=obj.id).order_by('index'):
            photos_html += f'<a href="/admin/main/productphoto/{p.id}/change/"><img style="margin: 5px"' \
                           f' src="{p.photo.url}" height=50></a>'
        return mark_safe(photos_html)
    get_html_photos.short_description = "Фото"


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'comment', 'rating', 'date_of_creation')


admin.site.register(Review, ReviewAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    fields = ('id', 'name', 'description')
    readonly_fields = ('id',)


admin.site.register(Material, MaterialAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug', 'id')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('id', 'name', 'slug', 'get_html_photo', 'photo', 'description')
    readonly_fields = ('id', 'get_html_photo')

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=50>")
    get_html_photo.short_description = "Фото"


admin.site.register(Manufacturer, ManufacturerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent_category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug', 'id')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('id', 'name', 'slug', 'get_html_photo', 'photo', 'description', 'parent_category')
    readonly_fields = ('id', 'get_html_photo')

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=50>")
    get_html_photo.short_description = "Фото"


admin.site.register(Category, CategoryAdmin)


class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'photo', 'product')
    list_display_links = ('id', 'photo')
    search_fields = ('id', 'photo')
    fields = ('id', 'get_html_photo', 'photo', 'index', 'product')
    readonly_fields = ('id', 'get_html_photo')

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=50>")
    get_html_photo.short_description = "Фото"


admin.site.register(ProductPhoto, ProductPhotoAdmin)
