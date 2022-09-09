from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from artefacts.models import Artefact
from artefacts.serializers import ArtefactSerializer


class ArtefactView(APIView):
    def get(self, request):
        artefacts_db = Artefact.objects.all()
        artefacts_serializer = ArtefactSerializer(instance=artefacts_db, many=True)
        return Response(
            data={"result": artefacts_serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def put(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response(data={"test": "message"}, status=status.HTTP_200_OK)
