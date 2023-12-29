from django.db import models
from model_utils import models as model_utils_models

from myapp.models import base_models


class Page(base_models.AuditedModel, model_utils_models.SoftDeletableModel, model_utils_models.TimeStampedModel):
    id = models.BigAutoField(
        primary_key=True,
        db_column='page_id',
    )

    slug = models.SlugField(
        max_length=128,
        unique=True,
    )

    title = models.CharField(
        max_length=256,
    )

    message = models.TextField(
    )

    status = models.CharField(
        max_length=32,
        default='NORMAL',
    )

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        db_table = 'content_page'
