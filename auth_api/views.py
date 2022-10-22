from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_api.models import User
from auth_api.serializers import UserSerializer, CustomObtainPairSerializer

from base.base_view import BaseView


class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class RegisterView(BaseView):
    model = User
    model_serializer = UserSerializer

    def post(self, request: Request) -> Response:
        serializer = self.model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_response_created(value=serializer.data)
        return self.get_response_bad_request(value=serializer.errors)
