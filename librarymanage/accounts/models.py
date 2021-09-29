from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BookUser(AbstractBaseUser):
    username = models.EmailField(
        verbose_name="Username", max_length=60, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
