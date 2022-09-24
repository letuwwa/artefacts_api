import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=False)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
