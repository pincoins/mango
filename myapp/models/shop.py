from django.db import models
from model_utils import models as model_utils_models


class Category(model_utils_models.TimeStampedModel):
    description = models.TextField(
        blank=True,
    )

    sub_description = models.TextField(
        blank=True,
    )

    discount_rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'


class Product(model_utils_models.SoftDeletableModel, model_utils_models.TimeStampedModel):
    name = models.CharField(
        max_length=255,
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
    )

    code = models.SlugField(
        max_length=255,
        unique=True,
        allow_unicode=True,
    )

    description = models.TextField(
        blank=True,
    )

    position = models.IntegerField(
    )

    # Max = 999,999,999.99
    list_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
    )

    selling_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
    )

    category = models.ForeignKey(
        'myapp.Category',
        db_index=True,
        on_delete=models.CASCADE,
    )

    stock_quantity = models.IntegerField(
        default=0,
    )

    minimum_stock_level = models.IntegerField(
        default=0,
    )

    maximum_stock_level = models.IntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'
