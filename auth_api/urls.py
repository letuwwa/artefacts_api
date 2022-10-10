from django.urls import path
from auth_api.views import RegisterView, CustomObtainPairView
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", CustomObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
