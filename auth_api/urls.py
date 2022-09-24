from django.urls import path
from auth_api.views import RegisterView, LoginView


urlpatterns = [
    path("login/", LoginView.as_view()),
    path("register/", RegisterView.as_view()),
]
