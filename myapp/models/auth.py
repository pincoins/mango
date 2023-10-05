from django.db import models
from model_utils import models as model_utils_models


class User(model_utils_models.TimeStampedModel):
    password = models.CharField(
        max_length=128,
    )

    username = models.CharField(
        unique=True,
        max_length=150,
    )

    email = models.EmailField(
    )

    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=False,
    )

    role = models.ForeignKey(
        'myapp.Role',
        db_index=True,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class Role(models.Model):
    code = models.CharField(
        unique=True,
        max_length=150,
    )

    name = models.CharField(
        max_length=150,
    )

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'
        db_table = 'role'
