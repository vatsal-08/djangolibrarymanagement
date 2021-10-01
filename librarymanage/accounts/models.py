from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, phone_no, password=None):
        if not email:
            raise ValueError("Email required")
        if not phone_no:
            raise ValueError("Please enter valid phone number")

        user = self.model(
            email=self.normalize_email(email),
            phone_no=phone_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_no, password=None):
        user = self.create_user(
            email=email,
            phone_no=phone_no,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BookUser(AbstractBaseUser):
    username = models.EmailField(
        verbose_name="Username", max_length=60, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    phone_no = models.CharField(max_length=20, verbose_name="Phone")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email', 'phone_no']

    objects = MyUserManager()

    def __str__(self):
        return self.username
