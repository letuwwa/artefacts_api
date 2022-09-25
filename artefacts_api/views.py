from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from artefacts_api.base.base_view import BaseView
from artefacts_api.models import Artefact, Archeologist
from artefacts_api.serializers import ArtefactSerializer, ArcheologistSerializer

from celery_app.tasks import create_artefact_copy


class ArtefactCommonView(BaseView):
    model = Artefact
    model_serializer = ArtefactSerializer

    def get(self, request: Request) -> Response:
        artefacts = self.model.objects.all()
        serializer = self.model_serializer(instance=artefacts, many=True)
        return self.get_response_ok(value=serializer.data)

    def post(self, request: Request) -> Response:
        serializer = self.model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            create_artefact_copy(serializer=serializer)
            return self.get_response_created(value=serializer.data)
        return self.get_response_bad_request(value=serializer.errors)


class ArcheologistCommonView(BaseView):
    model = Archeologist
    model_serializer = ArcheologistSerializer

    def get(self, request: Request, uuid: str):
        if archeologist := self.get_entity_or_none(pk=uuid):
            artefacts = Artefact.objects.all().filter(archeologist__id=archeologist.id)
            archeologist_serializer = self.model_serializer(instance=archeologist)
            artefacts_serializer = ArtefactSerializer(instance=artefacts, many=True)
            return self.get_response_ok(
                value={
                    "archeologist": archeologist_serializer.data,
                    "artefacts_api": artefacts_serializer.data,
                }
            )
        return self.get_response_not_found()


class ArtefactEntityView(BaseView):
    model = Artefact
    model_serializer = ArtefactSerializer

    def get(self, request: Request, pk: str) -> Response:
        if artefact := self.get_entity_or_none(pk=pk):
            return self.get_response_ok(value=self.model_serializer(artefact).data)
        return self.get_response_not_found()

    def put(self, request: Request, pk: str) -> Response:
        if artefact := self.get_entity_or_none(pk=pk):
            serializer = self.model_serializer(instance=artefact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return self.get_response_created(value=serializer.data)
            return self.get_response_bad_request(value=serializer.errors)
        return self.get_response_not_found()

    def delete(self, request: Request, pk: str) -> Response:
        if artefact := self.get_entity_or_none(pk=pk):
            artefact.delete()
            return self.get_response_deleted()
        return self.get_response_not_found()


@api_view()
def root_view(request):
    return Response({"message": "Hello, world!"})
