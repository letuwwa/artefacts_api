from rest_framework import serializers
from artefacts_api.models import Artefact, Archeologist


class ArcheologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archeologist
        fields = ("id", "name")


class ArtefactSerializer(serializers.ModelSerializer):
    archeologist = ArcheologistSerializer()

    class Meta:
        model = Artefact
        fields = "__all__"
