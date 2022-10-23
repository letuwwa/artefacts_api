from django.contrib import admin
from artefacts_api.models import Artefact, Archeologist, Article, HistoryAge


admin.site.register(Article)
admin.site.register(Artefact)
admin.site.register(HistoryAge)
admin.site.register(Archeologist)
