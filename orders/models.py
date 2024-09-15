from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    notes = models.CharField(max_length=500, blank=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.PositiveIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} for {self.user_first_name} {self.user_last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} : {self.product.name} x {self.quantity} (price: {self.price})'
