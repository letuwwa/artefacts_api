from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("artefacts/", include("artefacts_api.urls")),
    path("auth/", include("auth_api.urls")),
]
