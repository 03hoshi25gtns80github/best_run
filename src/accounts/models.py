from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(AbstractUser.Meta):
        verbose_name_plural = 'CustomUser'

# Create your models here.
