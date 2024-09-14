from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from cart.forms import AddToCartForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart_view(request, product_id):
    form = AddToCartForm(request.POST)
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product, int(cleaned_data.get('quantity')))

    return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.remove(product)

    return redirect('cart:cart_detail')


def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
