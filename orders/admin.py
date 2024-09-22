from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'phone_number', 'address', 'notes', 'is_paid', 'total_price')
    inlines = [OrderItemInline, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
