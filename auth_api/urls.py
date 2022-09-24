from django.urls import path
from auth_api.views import RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view()),
]
