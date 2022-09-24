import os

import jwt
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from auth_api.models import User
from auth_api.serializers import UserSerializer
from artefacts.base.base_response_class import BaseResponse


class RegisterView(APIView, BaseResponse):
    def post(self, request: Request) -> Response:
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return self.get_response_created(value=user_serializer.data)
        return self.get_response_bad_request(value=user_serializer.errors)


class LoginView(APIView, BaseResponse):
    def post(self, request: Request) -> Response:
        if not (email := request.data.get("email")):
            return self.get_response_bad_request()

        if not (password := request.data.get("password")):
            return self.get_response_bad_request()

        if not (user := User.objects.filter(email=email).first()):
            return self.get_response_forbidden()

        if not user.check_password(raw_password=password):
            return self.get_response_forbidden()

        payload = {
            "id": str(user.id),
            "iat": datetime.now(),
            "exp": datetime.now() + timedelta(minutes=30),
        }

        token = jwt.encode(
            payload=payload,
            algorithm="HS256",
            key=os.environ.get("jwt_secret_key"),
        )

        response = self.get_response_ok(value={"jwt": token})
        response.set_cookie(key="jwt", value=token, httponly=True)

        return response
