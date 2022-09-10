from django.urls import path
from .apps import ArtefactsConfig
from .views import ArtefactCommonView, root_view


app_name = ArtefactsConfig.name

urlpatterns = [
    path("", root_view),
    path("artefact/", ArtefactCommonView.as_view()),
]
