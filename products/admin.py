from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')


admin.site.register(Product, ProductAdmin)
