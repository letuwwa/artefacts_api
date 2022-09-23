from rest_framework import status
from rest_framework.response import Response


class BaseResponse:
    @staticmethod
    def get_response_not_found() -> Response:
        return Response(data={"status": "not_found"}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def get_response_deleted() -> Response:
        return Response(data={"status": "deleted"}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_response_ok(value) -> Response:
        return Response(data=value, status=status.HTTP_200_OK)

    @staticmethod
    def get_response_bad_request(value) -> Response:
        return Response(data=value, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_response_created(value) -> Response:
        return Response(data=value, status=status.HTTP_201_CREATED)
