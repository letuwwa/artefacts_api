from rest_framework import serializers
from artefacts_api.models import Artefact, Archeologist, HistoryAge, Article


class HistoryAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryAge
        fields = "__all__"


class ArcheologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archeologist
        fields = ("id", "first_name", "surname", "email")


class ArtefactSerializer(serializers.ModelSerializer):
    archeologist = ArcheologistSerializer(allow_null=True, required=False)

    class Meta:
        model = Artefact
        fields = "__all__"

    def validate(self, data):
        """
        This check should affect values of creation_year and discovery_year
        """
        creation_year = data.get("creation_year")
        discovery_year = data.get("discovery_year")

        if discovery_year and creation_year and creation_year >= discovery_year:
            raise serializers.ValidationError(
                "creation_year can't be greater or equal to discovery_year"
            )

        return data


class ArticleSerializer(serializers.ModelSerializer):
    artefacts = ArtefactSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "text", "artefacts")
