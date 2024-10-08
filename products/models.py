from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='products/covers/', verbose_name=_('product cover'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id])


# class ActiveCommentManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    body = models.TextField(verbose_name=_("Comment Text"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments",
                               verbose_name='Comment Author')
    star = models.CharField(max_length=1, choices=PRODUCT_STARS, verbose_name=_('Product Star'))
    is_active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # manager
    # objects = models.Manager()
    # active_comments = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
