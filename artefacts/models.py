import uuid
from django.db.models import Model, CharField, UUIDField


class Artefact(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=128, null=False, help_text="Name")
    description = CharField(max_length=2048, null=True, help_text="Description")

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = "Artefact"
        verbose_name_plural = "Artefacts"
