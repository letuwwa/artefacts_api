from artefacts.models import Artefact, Archeologist
from rest_framework.serializers import ModelSerializer


class ArtefactSerializer(ModelSerializer):
    class Meta:
        model = Artefact
        fields = "__all__"


class ArcheologistSerializer(ModelSerializer):
    class Meta:
        model = Archeologist
        fields = "__all__"
