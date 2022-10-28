from django.db.models import Q
from rest_framework.request import Request
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from base import BaseView
from artefacts_api.models import Artefact, Archeologist, HistoryAge, Article
from artefacts_api.serializers import (
    ArticleSerializer,
    ArtefactSerializer,
    HistoryAgeSerializer,
    ArcheologistSerializer,
)

from celery_app.tasks import create_archeologists, create_artefacts


class ArticleCommonView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleEntityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class HistoryAgeCommonView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = HistoryAge.objects.all()
    serializer_class = HistoryAgeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HistoryAgeEntityView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = HistoryAge.objects.all()
    serializer_class = HistoryAgeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArtefactCommonView(BaseView):
    model = Artefact
    model_serializer = ArtefactSerializer

    def get(self, request: Request) -> Response:
        artefacts = self.model.objects.all()
        serializer = self.model_serializer(instance=artefacts, many=True)
        return self.get_response_ok(value={"artefacts": serializer.data})

    def post(self, request: Request) -> Response:
        serializer = self.model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_response_created(value=serializer.data)
        return self.get_response_bad_request(value=serializer.errors)


class ArcheologistCommonView(BaseView):
    model = Archeologist
    model_serializer = ArcheologistSerializer

    def get(self, request: Request) -> Response:
        archeologists = self.model.objects.all()
        serializer = self.model_serializer(instance=archeologists, many=True)
        return self.get_response_ok(value={"archeologists": serializer.data})


class ArcheologistEntityView(BaseView):
    model = Archeologist
    model_serializer = ArcheologistSerializer
    permission_classes = [
        IsAuthenticated,
    ]

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

    def get(self, request: Request, uuid: str) -> Response:
        if artefact := self.get_entity_or_none(pk=uuid):
            return self.get_response_ok(value=self.model_serializer(artefact).data)
        return self.get_response_not_found()

    def put(self, request: Request, uuid: str) -> Response:
        if artefact := self.get_entity_or_none(pk=uuid):
            serializer = self.model_serializer(instance=artefact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return self.get_response_created(value=serializer.data)
            return self.get_response_bad_request(value=serializer.errors)
        return self.get_response_not_found()

    def delete(self, request: Request, uuid: str) -> Response:
        if artefact := self.get_entity_or_none(pk=uuid):
            artefact.delete()
            return self.get_response_deleted()
        return self.get_response_not_found()


@api_view()
def artefact_root_view(request):
    artefacts_queryset = Artefact.objects.filter(
        Q(creation_year__gt=1000) & Q(discovery_year__gt=2005) & ~Q(archeologist=None)
    )[:5]
    artefacts_serializer = ArtefactSerializer(instance=artefacts_queryset, many=True)
    return Response(
        {
            "data": artefacts_serializer.data,
            "query": str(artefacts_queryset.query),
        }
    )


@api_view()
def db_artefacts_view(request):
    result = create_artefacts.apply_async(countdown=1)
    result.get()
    return Response({"status": "created"})


@api_view()
def db_archeologists_view(request):
    result = create_archeologists.apply_async(countdown=1)
    result.get()
    return Response({"status": "created"})
