from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager 


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length = 30, unique = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
