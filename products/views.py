from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail_view.html'