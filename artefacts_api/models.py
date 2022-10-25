from base import BaseModel
from django.db import models


class Archeologist(BaseModel):
    first_name = models.CharField(max_length=128, null=False, help_text="Name")
    surname = models.CharField(max_length=128, null=False, help_text="Surname")
    email = models.EmailField(max_length=254, null=True, help_text="Email")

    def __str__(self) -> str:
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = "Archeologist"
        verbose_name_plural = "Archeologists"


class HistoryAge(BaseModel):
    title = models.CharField(max_length=128, null=False, blank=False, help_text="Title")
    description = models.CharField(max_length=2048, null=True, help_text="Description")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "History Age"
        verbose_name_plural = "History Ages"


class Artefact(BaseModel):
    name = models.CharField(max_length=128, null=False, help_text="Name")
    description = models.CharField(max_length=2048, null=True, help_text="Description")
    creation_year = models.IntegerField(
        blank=True, null=True, help_text="Year of creation"
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
    history_age = models.OneToOneField(
        null=True,
        blank=True,
        to=HistoryAge,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Artefact"
        verbose_name_plural = "Artefacts"


class Article(BaseModel):
    title = models.CharField(max_length=128, null=False, blank=False, help_text="Title")
    text = models.TextField(null=False, blank=False, help_text="Text")
    artefacts = models.ManyToManyField(to=Artefact)
    archeologists = models.ManyToManyField(to=Archeologist)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
