from artefacts.models import Artefact
from rest_framework.serializers import ModelSerializer


class ArtefactSerializer(ModelSerializer):
    class Meta:
        model = Artefact
        fields = "__all__"
