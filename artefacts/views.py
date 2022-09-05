from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ArtefactView(APIView):
    def get(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def put(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)
