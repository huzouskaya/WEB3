from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')
    type = models.CharField(max_length=25, unique=False, blank=True, verbose_name='Тип')

    class Meta:
        verbose_name: 'Категорию'
        verbose_name_plural: 'Категории'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.CharField(max_length=400, unique=True, blank=True, null=True, verbose_name='URL изображения')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ManyToManyField(to=Categories, verbose_name='Категория')
    size = models.CharField(max_length=1, blank=True, null=True, verbose_name='Размер')
    country = models.CharField(max_length=150, verbose_name='Страна производителя')
    material = models.CharField(max_length=200, verbose_name='Материал')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return self.name