from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255,null=False)
    email = models.CharField(max_length=255,null=False, unique=True)
    password = models.CharField(max_length=255,null=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []