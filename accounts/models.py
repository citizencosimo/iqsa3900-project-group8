from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.username
# Create your models here.
