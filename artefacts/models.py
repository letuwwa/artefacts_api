import uuid
from django.db import models


class Artefact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False, help_text="Name")
    description = models.CharField(max_length=2048, null=True, help_text="Description")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Artefact"
        verbose_name_plural = "Artefacts"
