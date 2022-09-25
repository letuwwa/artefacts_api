# Generated by Django 4.1 on 2022-09-25 11:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archeologist",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(help_text="Name", max_length=128)),
                ("surname", models.CharField(help_text="Surname", max_length=128)),
                (
                    "email",
                    models.EmailField(help_text="Email", max_length=254, null=True),
                ),
            ],
            options={
                "verbose_name": "Archeologist",
                "verbose_name_plural": "Archeologists",
            },
        ),
        migrations.CreateModel(
            name="Artefact",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(help_text="Name", max_length=128)),
                (
                    "description",
                    models.CharField(
                        help_text="Description", max_length=2048, null=True
                    ),
                ),
                (
                    "archeologist",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="artefacts_api.archeologist",
                    ),
                ),
            ],
            options={
                "verbose_name": "Artefact",
                "verbose_name_plural": "Artefacts",
            },
        ),
    ]
