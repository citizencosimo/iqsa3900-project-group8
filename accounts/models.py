from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_onprobation = models.BooleanField(default=False,
                                         help_text="Designates whether this user in on probation for innapropriate conduct.",
                                         verbose_name="probation status")
    moderation_message = models.CharField(max_length=1000, help_text="Explanation of why the use has been put on probation or banned.", blank=True, null=True)
    def __str__(self):
        return self.username
# Create your models here.

class Developer(models.Model)
    Developer_ID = models.Autofield(primary_key=True)
    Developer_Name = models.CharField(max_length=1000)
    Developer_Image = models.ImageField(upload_to='images/')
    Developer_Country = models. CharField(max_length=500)
    Developer_Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Developer_Name