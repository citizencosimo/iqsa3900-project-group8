import os
import uuid

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


def generate_unique_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{extension}"
    return os.path.join('user_images/', new_filename)

class CustomFileSystemStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not os.path.exists(self.location):
            os.makedirs(self.location)

class CustomUser(AbstractUser):
    pass
    user_image = models.ImageField(upload_to=generate_unique_filename, storage=CustomFileSystemStorage(), null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_onprobation = models.BooleanField(default=False,
                                         help_text="Designates whether this user in on probation for innapropriate conduct.",
                                         verbose_name="probation status")
    moderation_message = models.CharField(max_length=1000,
                                          help_text="Explanation of why the user has been put on probation or banned.",
                                          blank=True, null=True)

    def __str__(self):
        return self.username

@receiver(pre_save, sender=CustomUser)
def deleteOldImage(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = CustomUser.objects.get(pk=instance.pk)
            if old_instance.user_image and instance.user_image != old_instance.user_image:
                old_instance.user_image.delete(save=False)
        except CustomUser.DoesNotExist:
            pass
