import uuid

from accounts import models
from django.db import models


# Create your models here.
class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=25)
    platform_image = models.ImageField(upload_to='platform_images/')
    platform_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.platform_name

