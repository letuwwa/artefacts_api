# Generated by Django 4.1 on 2022-10-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artefacts_api", "0004_alter_historyage_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="archeologists",
            field=models.ManyToManyField(to="artefacts_api.archeologist"),
        ),
    ]
