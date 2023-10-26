from decimal import Decimal

from django.db import models
from model_utils import models as model_utils_models


class User(model_utils_models.TimeStampedModel):
    id = models.BigAutoField(
        primary_key=True,
        db_column='user_id'
    )

    password = models.CharField(
        max_length=128,
    )

    username = models.CharField(
        unique=True,
        max_length=150,
    )

    email = models.EmailField(
        unique=True,
        max_length=150,
    )

    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=32,
        db_index=True,
        default='NORMAL',
    )

    role = models.CharField(
        max_length=32,
        db_index=True,
        default='ROLE_MEMBER',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class Profile(model_utils_models.TimeStampedModel):
    id = models.BigAutoField(
        primary_key=True,
        db_column='profile_id'
    )

    user = models.OneToOneField(
        'myapp.User',
        db_index=True,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    domestic = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    telecom = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    phone_verified_status = models.CharField(
        max_length=32,
        db_index=True,
        default='UNVERIFIED',
    )

    photo_id = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    card = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    document_verified_status = models.CharField(
        max_length=32,
        db_index=True,
        default='UNVERIFIED',
    )

    allow_order = models.BooleanField(
        default=False,
    )

    total_order_count = models.IntegerField(
        default=0,
    )

    first_purchased = models.DateTimeField(
        null=True,
    )

    last_purchased = models.DateTimeField(
        null=True,
    )

    not_purchased_months = models.BooleanField(
        default=False,
    )

    repurchased = models.DateTimeField(
        null=True,
    )

    max_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

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

    average_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    mileage = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    memo = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        db_table = 'profile'
