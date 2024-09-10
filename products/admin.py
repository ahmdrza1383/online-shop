from django.contrib import admin

from products.models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    inlines = [CommentInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'star', 'body', 'is_active')


admin.site.register(Product, ProductAdmin)
