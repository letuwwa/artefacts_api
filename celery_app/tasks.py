from faker import Faker
from .celery import app
from random import randint, choice
from artefacts_api.models import Archeologist, Artefact


faker = Faker()


@app.task
def create_archeologists(archeologists_count: int = 5) -> None:
    for _ in range(archeologists_count):
        archeologist = Archeologist()
        archeologist.first_name = faker.first_name()
        archeologist.surname = faker.last_name()
        archeologist.email = faker.email()
        archeologist.save()


@app.task
def create_artefacts(artefacts_count: int = 15) -> None:
    archeologists = list(Archeologist.objects.all())
    for _ in range(artefacts_count):
        artefact = Artefact()
        artefact.name = faker.catch_phrase()
        artefact.description = faker.paragraph(nb_sentences=1)
        artefact.creation_year = randint(0, 1999)
        artefact.discovery_year = randint(2000, 2022)
        artefact.archeologist = choice(archeologists)
        artefact.save()
