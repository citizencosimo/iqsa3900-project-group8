import uuid

from accounts import models
from django.db import models

class Language(models.Model):
    language_name = models.CharField(max_length=25, default="Unknown")
    language_charset = models.CharField(max_length=25, default="Unknown", help_text="The alphabet used by the language. Currently unused")
class Genre(models.Model):
    genre_name = models.CharField(max_length=200, help_text="The genre(s) of the game.")
    genre_description = models.CharField(max_length=200, blank="True", null="True")

class Publisher(models.model):
    publisher_id = models.IntegerField(max_length=8, primary_key=True)
    publisher_name = models.CharField(max_length=1000)
    publisher_image = models.ImageField(upload_to='images/', null=True, blank=True)
    publisher_country = models.CharField(max_length=500)
    publisher_description = models.CharField(max_length=1000)
    def __str__(self):
        return self.publisher_name

class Developer(models.Model):
    developer_id = models.Autofield(primary_key=True)
    developer_name = models.CharField(max_length=1000)
    developer_image = models.ImageField(upload_to='images/')
    developer_country = models.CharField(max_length=500)
    developer_description = models.CharField(max_length=1000)
    def __str__(self):
        return self.developer_name

class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=25)
    platform_image = models.ImageField(upload_to='platform_images/')
    platform_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.platform_name

