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
    path("artefacts/", ArtefactCommonView.as_view()),
    path("artefacts/<str:uuid>/", ArtefactEntityView.as_view()),
    path("archeologists/<str:uuid>/", ArcheologistCommonView.as_view()),
]
