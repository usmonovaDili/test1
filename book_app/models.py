from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (3, 'admin'),
        (2, 'author'),
        (1, 'user')
    )
    role = models.PositiveSmallIntegerField(default=1, choices=CHOICE_ROLES)
    phone = models.CharField(default='', max_length=15)
