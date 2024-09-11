from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.utils.translation import gettext as _

from .forms import CommentForm
from .models import Product, Comment


class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail_view.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['active_comments'] = Product.objects.get(pk=self.kwargs['pk']).comments.filter(is_active=True)
        data['comment_form'] = CommentForm()
        return data


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, _('You must be logged in.'))
            return redirect('account_login')
        else:
            return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        obj.product = product

        return super().form_valid(form)

# def get_success_url(self):
#     return reverse_lazy('product_detail', args=[self.kwargs['pk']])
