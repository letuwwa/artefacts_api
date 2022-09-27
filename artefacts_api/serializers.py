from rest_framework import serializers
from artefacts_api.models import Artefact, Archeologist


class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = "__all__"


class ArcheologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archeologist
        fields = "__all__"
