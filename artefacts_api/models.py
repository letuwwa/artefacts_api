import uuid
from django.db import models


class Archeologist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False, help_text="Name")
    surname = models.CharField(max_length=128, null=False, help_text="Surname")
    email = models.EmailField(max_length=254, null=True, help_text="Email")

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Archeologist"
        verbose_name_plural = "Archeologists"


class Artefact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False, help_text="Name")
    description = models.CharField(max_length=2048, null=True, help_text="Description")
    creation_century = models.IntegerField(
        blank=True, null=True, help_text="Century of creation"
    )
    discovery_year = models.IntegerField(
        blank=True, null=True, help_text="Year of discovery"
    )
    archeologist = models.ForeignKey(
        null=True,
        blank=True,
        to=Archeologist,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.name} by {self.archeologist}"

    class Meta:
        verbose_name = "Artefact"
        verbose_name_plural = "Artefacts"
