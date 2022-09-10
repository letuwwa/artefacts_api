from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Model

from artefacts.models import Artefact
from artefacts.serializers import ArtefactSerializer


class ArtefactCommonView(APIView):
    def get(self, request: Request) -> Response:
        artefacts = Artefact.objects.all()
        serializer = ArtefactSerializer(instance=artefacts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ArtefactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtefactEntityView(APIView):
    def get(self, request: Request, pk: str) -> Response:
        artefact = self.get_artefact_or_none(pk=pk)
        if artefact:
            return Response(data=ArtefactSerializer(artefact).data, status=status.HTTP_200_OK)
        return Response(data={"message": "not_found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request) -> Response:
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    @staticmethod
    def get_artefact_or_none(pk: str) -> Model | None:
        try:
            return Artefact.objects.get(pk=pk)
        except Artefact.DoesNotExist:
            return None


@api_view()
def root_view(request):
    return Response({"message": "Hello, world!"})
