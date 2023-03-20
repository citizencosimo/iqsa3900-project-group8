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
