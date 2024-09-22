from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem


def order_create_view(request):
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('You have not selected any products to buy.'))
        return redirect('products_list')

    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST, )

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.is_paid = False
            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            messages.success(request, _('Your order has been submitted.'))
            cart.clear()

            return redirect('products_list')

    return render(request, 'orders/order_create.html', {
        'order_form': order_form,
    })
