from rest_framework.views import APIView
from rest_framework.request import Request

from auth_api.serializers import UserSerializer
from artefacts.base.base_response_class import BaseResponse


class RegisterView(APIView, BaseResponse):
    def post(self, request: Request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return self.get_response_created(value=user_serializer.data)
        return self.get_response_bad_request(value=user_serializer.errors)
