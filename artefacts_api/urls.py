from django.urls import path
from .apps import ArtefactsConfig
from .views import (
    ArtefactCommonView,
    ArtefactEntityView,
    ArcheologistCommonView,
    ArcheologistEntityView,
    db_artefacts_view,
    db_archeologists_view,
)


app_name = ArtefactsConfig.name

urlpatterns = [
    path("create_artefacts/", db_artefacts_view),
    path("create_archeologists/", db_archeologists_view),
    path("artefacts/", ArtefactCommonView.as_view()),
    path("artefacts/<str:uuid>/", ArtefactEntityView.as_view()),
    path("archeologists/", ArcheologistCommonView.as_view()),
    path("archeologists/<str:uuid>/", ArcheologistEntityView.as_view()),
]
