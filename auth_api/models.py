from base import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=128, verbose_name="First Name")
    last_name = models.CharField(max_length=128, verbose_name="Last Name")
    password = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=128, verbose_name="Username")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
