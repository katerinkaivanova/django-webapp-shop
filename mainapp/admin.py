from django.contrib import admin
from mainapp.models import Product, ProductCategory


class ProductInline(admin.TabularInline):
    model = Product
    fields = 'name', 'short_desc'
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = ProductInline,


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = 'name', 'category__name',
    list_display = 'name', 'category', 'price', 'quantity',
    #readonly_fields = 'price',
