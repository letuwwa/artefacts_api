from rest_framework import serializers
from artefacts_api.models import Artefact, Archeologist


class ArcheologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archeologist
        fields = ("id", "name")


class ArtefactSerializer(serializers.ModelSerializer):
    archeologist = ArcheologistSerializer(allow_null=True)

    class Meta:
        model = Artefact
        fields = "__all__"

    def validate(self, data):
        creation_year = data.get("creation_year")
        discovery_year = data.get("discovery_year")

        if discovery_year and creation_year:
            if creation_year >= discovery_year:
                raise serializers.ValidationError(
                    "creation_year can't be greater or equal to discovery_year"
                )

        return data
