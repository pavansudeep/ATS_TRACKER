from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username
