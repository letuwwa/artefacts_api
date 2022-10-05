from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from artefacts_api.base.base_response_class import ResponseMixin


class BaseView(APIView, ResponseMixin):
    model: Model
    model_serializer: ModelSerializer

    @classmethod
    def get_entity_or_none(cls, pk: str) -> Model | None:
        try:
            return cls.model.objects.get(pk=pk)
        except cls.model.DoesNotExist:
            return None
