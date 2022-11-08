from django.db import models


# Create your models here.

class Product(models.Model):
    ON_SALE = "S"
    STATUS_TYPES = (
        ("A", "Архивный товар"),
        (ON_SALE, "В наличии"),
        ("E", "Ожидается"),
    )

    KIT_TYPE = (
        ("RTR", "(RTR)Ready to Run"),
        ("RTF", "(RTF)Ready to Fly"),
        ("PNP", "(PNP)Plug and Play"),
        ("BND", "(BND)Bind and Drive"),
        ("BNF", "(BNF)Bind and Fly"),
        ("KIT", "KIT"),
        (None, "Не указан"),
    )

    ENGINE_TYPE = (
        ("B", "Коллекторный"),
        ("BL", "Бесколлекторный"),
        ("ICE", "ДВС"),
        (None, "Без двигателя"),
    )

    POWER_SUPPLY = (
        ("B", "Батарейка"),
        ("A", "Аккумулятор"),
        (None, "Не указан"),
    )

    CHANNEL_FREQUENCY = (
        ("CF1", "27 МГц"),
        ("CF2", "40 МГц"),
        ("CF3", "2.4 ГГц"),
        (None, "Не указан"),
    )

    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    discount = models.FloatField(verbose_name="Скидка", blank=True, null=True)
    average_rating = models.FloatField(verbose_name="Средний рейтинг", default=0.0)
    num_of_reviews = models.PositiveSmallIntegerField(verbose_name="Количество отзывов", default=0)
    product_code = models.PositiveIntegerField(unique=True, verbose_name="Код товара")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    status = models.CharField(max_length=5, choices=STATUS_TYPES, verbose_name="Статус", default=ON_SALE, null=True)
    warranty_period = models.CharField(max_length=255, verbose_name="Гарантийный срок", blank=True, null=True)
    return_period = models.CharField(max_length=255, verbose_name="Обмен/возврат", blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name="Количество товара в наличии")
    slug = models.SlugField(max_length=255, unique=True)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, verbose_name="Производитель")
    material = models.ManyToManyField('Material', verbose_name="Материал корпуса", blank=True)
    model_power_supply = models.CharField(max_length=1, choices=POWER_SUPPLY, verbose_name="Источник питания модели",
                                          null=True, blank=True)
    r_controller_power_supply = models.CharField(max_length=1, choices=POWER_SUPPLY,
                                                 verbose_name="Источник питания пульта", null=True, blank=True)
    engine_type = models.CharField(max_length=3, choices=ENGINE_TYPE, verbose_name="Тип двигателя",
                                   null=True, blank=True)
    channel_frequency = models.CharField(max_length=5, choices=CHANNEL_FREQUENCY, verbose_name="Частота",
                                         null=True, blank=True)
    num_of_channels = models.PositiveSmallIntegerField(verbose_name="Количество каналов", blank=True, null=True)
    camera_presence = models.BooleanField(default=False, verbose_name="С камерой")
    kit_type = models.CharField(max_length=3, choices=KIT_TYPE, verbose_name="Тип комплектации", null=True, blank=True)
    length = models.PositiveSmallIntegerField(verbose_name="Длина в(мм)", blank=True, null=True)
    height = models.PositiveSmallIntegerField(verbose_name="Высота в(мм)", blank=True, null=True)
    width = models.PositiveSmallIntegerField(verbose_name="Ширина в(мм)", blank=True, null=True)
    complete_set = models.TextField(verbose_name="В комплекте", blank=True, null=True)
    packing_size = models.CharField(max_length=255, verbose_name="Габариты упаковки", blank=True, null=True)
    feature = models.TextField(verbose_name="Особенности", blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации товара")

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['average_rating']
        get_latest_by = "date_of_creation"

    def __str__(self):
        return self.title


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/manufacturer/%Y/%m/%d/", blank=True, null=True, verbose_name="Фото")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/category/%Y/%m/%d/", blank=True, null=True, verbose_name="Фото")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name="Родительская категория")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to="photos/product/%Y/%m/%d/", verbose_name="Фото")
    index = models.PositiveSmallIntegerField(verbose_name="Номер")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'
        ordering = ['product']

    def __str__(self):
        return f"id({self.pk}) {self.index} - {self.photo}"

