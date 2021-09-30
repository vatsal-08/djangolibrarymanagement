from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BookUser(AbstractBaseUser):
    username = models.EmailField(
        verbose_name="Username", max_length=60, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    phone = models.CharField(max_length=20, verbose_name="Phone")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
