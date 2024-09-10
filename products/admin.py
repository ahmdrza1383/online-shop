from django.contrib import admin

from products.models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'star', 'body', 'is_active')


admin.site.register(Product, ProductAdmin)
