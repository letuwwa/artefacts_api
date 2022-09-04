from django.contrib import admin
from artefacts.models import Artefact


class ArtefactAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


admin.site.register(Artefact, ArtefactAdmin)
