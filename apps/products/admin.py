from django.contrib import admin

from apps.products.models import Product, Category, ProductImage


class ProductImageAdminInline(admin.TabularInline):
    extra = 4
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = ProductImageAdminInline,


class ProductInline(admin.StackedInline):
    extra = 4
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
