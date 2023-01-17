from drf_yasg import openapi
from logging import getLogger
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.urls import path, include, re_path
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_root(request: Request):
    getLogger().info("hola!")
    return Response(f"Hi!, {request.user}")


schema_view = get_schema_view(
    openapi.Info(
        title="Artefacts API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="letuwwa@gmail.com"),
        license=openapi.License(name="Free license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", api_root),
    re_path(
        r"^doc(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("auth_api/", include("auth_api.urls")),
    path("artefacts_api/", include("artefacts_api.urls")),
]
