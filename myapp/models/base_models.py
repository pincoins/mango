from django.db import models


class AuditedModel(models.Model):
    created_by = models.BigIntegerField(
        null=True,
    )

    last_modified_by = models.BigIntegerField(
        null=True,
    )

    class Meta:
        abstract = True
