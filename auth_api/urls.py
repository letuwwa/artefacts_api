from django.urls import path
from auth_api.views import RegisterView, AuthTokenView, AuthTokenRefreshView


urlpatterns = [
    path("token/", AuthTokenView.as_view()),
    path("token/refresh/", AuthTokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
]
