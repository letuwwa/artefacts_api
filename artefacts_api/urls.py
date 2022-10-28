from django.urls import path
from .apps import ArtefactsConfig
from .views import (
    ArticleCommonView,
    ArticleEntityView,
    ArtefactCommonView,
    ArtefactEntityView,
    HistoryAgeCommonView,
    HistoryAgeEntityView,
    ArcheologistCommonView,
    ArcheologistEntityView,
    db_artefacts_view,
    db_archeologists_view,
    artefact_root_view,
)


app_name = ArtefactsConfig.name

urlpatterns = [
    path("", artefact_root_view),
    path("articles/", ArticleCommonView.as_view()),
    path("articles/<str:pk>/", ArticleEntityView.as_view()),
    path("history_ages/", HistoryAgeCommonView.as_view()),
    path("history_ages/<str:pk>/", HistoryAgeEntityView.as_view()),
    path("create_artefacts/", db_artefacts_view),
    path("create_archeologists/", db_archeologists_view),
    path("artefacts/", ArtefactCommonView.as_view()),
    path("artefacts/<str:uuid>/", ArtefactEntityView.as_view()),
    path("archeologists/", ArcheologistCommonView.as_view()),
    path("archeologists/<str:uuid>/", ArcheologistEntityView.as_view()),
]
