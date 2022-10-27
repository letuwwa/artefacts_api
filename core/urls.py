from django.contrib import admin
from django.urls import path, include

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_root(request: Request):
    return Response(f"Hi!, {request.user}")


urlpatterns = [
    path("", api_root),
    path("admin/", admin.site.urls),
    path("auth_api/", include("auth_api.urls")),
    path("artefacts_api/", include("artefacts_api.urls")),
]
