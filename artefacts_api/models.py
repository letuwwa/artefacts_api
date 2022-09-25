import uuid
from django.db.models import (
    Model,
    CASCADE,
    CharField,
    UUIDField,
    EmailField,
    ForeignKey,
)


class Archeologist(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=128, null=False, help_text="Name")
    surname = CharField(max_length=128, null=False, help_text="Surname")
    email = EmailField(max_length=254, null=True, help_text="Email")

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Archeologist"
        verbose_name_plural = "Archeologists"


class Artefact(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=128, null=False, help_text="Name")
    description = CharField(max_length=2048, null=True, help_text="Description")
    archeologist = ForeignKey(to=Archeologist, on_delete=CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name} by {self.archeologist}"

    class Meta:
        verbose_name = "Artefact"
        verbose_name_plural = "Artefacts"
