from django.urls import path
from .views import ArtefactView
from .apps import ArtefactsConfig


app_name = ArtefactsConfig.name

urlpatterns = [path("", ArtefactView.as_view())]
