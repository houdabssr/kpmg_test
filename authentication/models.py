from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_dz = models.BooleanField(default=False)
    is_fr = models.BooleanField(default=False)