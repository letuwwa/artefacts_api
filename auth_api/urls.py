from django.urls import path
from auth_api.views import RegisterView


urlpatterns = [
    path("", RegisterView.as_view()),
]
