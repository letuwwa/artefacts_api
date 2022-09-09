from artefacts.models import Artefact
from rest_framework import serializers


class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = "__all__"
