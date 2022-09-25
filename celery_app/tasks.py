from .celery import app
from artefacts_api.models import Artefact
from artefacts_api.serializers import ArtefactSerializer


@app.task
def create_artefact_copy(serializer: ArtefactSerializer):
    artefact_copy = Artefact()
    artefact_copy.name = "COPY_" + serializer.initial_data.get("name")
    artefact_copy.description = serializer.initial_data.get("description")
    artefact_copy.archeologist = serializer.initial_data.get("archeologist")
    artefact_copy.save()
