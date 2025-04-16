from django.contrib import admin

from goods.models import Categories, Products

# user g-a223 password abcd1234

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields: {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields: {'slug': ('name',)}

