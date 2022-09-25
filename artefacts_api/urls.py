from django.urls import path
from .apps import ArtefactsConfig
from .views import (
    ArtefactCommonView,
    ArtefactEntityView,
    root_view,
    ArcheologistCommonView,
)


app_name = ArtefactsConfig.name

urlpatterns = [
    path("", root_view),
    path("archeologist/<str:uuid>/", ArcheologistCommonView.as_view()),
    path("artefact/", ArtefactCommonView.as_view()),
    path("artefact/<str:pk>/", ArtefactEntityView.as_view()),
]
