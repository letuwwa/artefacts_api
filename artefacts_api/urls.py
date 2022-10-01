from django.urls import path
from .apps import ArtefactsConfig
from .views import (
    root_view,
    ArtefactCommonView,
    ArtefactEntityView,
    ArcheologistCommonView,
)


app_name = ArtefactsConfig.name

urlpatterns = [
    path("", root_view),
    path("artefact/", ArtefactCommonView.as_view()),
    path("artefact/<str:uuid>/", ArtefactEntityView.as_view()),
    path("archeologist/<str:uuid>/", ArcheologistCommonView.as_view()),
]
