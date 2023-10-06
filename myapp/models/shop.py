import uuid
from decimal import Decimal

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


class Voucher(model_utils_models.SoftDeletableModel, model_utils_models.TimeStampedModel):
    product = models.ForeignKey(
        'myapp.Product',
        db_index=True,
        on_delete=models.PROTECT,
    )

    code = models.CharField(
        max_length=64,
    )

    remarks = models.CharField(
        max_length=64,
        blank=True,
    )

    class Meta:
        verbose_name = 'voucher'
        verbose_name_plural = 'vouchers'
        db_table = 'voucher'

        unique_together = ('product', 'code',)

        indexes = [
            models.Index(fields=['code', ]),
        ]


class Order(model_utils_models.TimeStampedModel):
    order_id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        'myapp.User',
        db_index=True,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
    )

    fullname = models.CharField(
        max_length=64,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    accept_language = models.TextField(
        blank=True,
    )

    ip_address = models.GenericIPAddressField(
    )

    payment_method = models.IntegerField(
        db_index=True,
    )

    transaction_id = models.CharField(
        max_length=64,
        blank=True,
    )

    status = models.IntegerField(
        db_index=True,
    )

    visible = models.IntegerField(
        db_index=True,
    )

    # Max = 999,999,999.99
    total_list_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    total_selling_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    message = models.TextField(
        blank=True,
    )

    parent = models.ForeignKey(
        'self',
        db_index=True,
        null=True,
        on_delete=models.CASCADE,
    )

    suspicious = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = 'pincoin order'
        verbose_name_plural = 'pincoin orders'
        db_table = 'order'


class OrderPayment(model_utils_models.TimeStampedModel):
    order = models.ForeignKey(
        'myapp.Order',
        db_index=True,
        on_delete=models.CASCADE,
    )

    account = models.IntegerField(
        db_index=True,
    )

    amount = models.DecimalField(
        max_digits=11,
        decimal_places=2,
    )

    balance = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    received = models.DateTimeField(
    )

    class Meta:
        verbose_name = 'order payment'
        verbose_name_plural = 'order payments'
        db_table = 'order_payment'


class OrderProduct(model_utils_models.TimeStampedModel):
    order = models.ForeignKey(
        'myapp.Order',
        db_index=True,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=255,
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
    )

    code = models.CharField(
        max_length=255,
    )

    # Max = 999,999,999.99
    list_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    selling_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    quantity = models.IntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'order product'
        verbose_name_plural = 'order products'
        db_table = 'order_product'


class OrderProductVoucher(model_utils_models.TimeStampedModel):
    order_product = models.ForeignKey(
        'myapp.OrderProduct',
        db_index=True,
        on_delete=models.CASCADE,
    )

    voucher = models.ForeignKey(
        'myapp.Voucher',
        db_index=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    code = models.CharField(
        max_length=64,
    )

    revoked = models.BooleanField(
        default=False,
    )

    remarks = models.CharField(
        max_length=64,
        blank=True,
    )

    class Meta:
        verbose_name = 'order product voucher'
        verbose_name_plural = 'order product vouchers'
        db_table = 'order_product_voucher'
