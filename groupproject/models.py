import uuid

from accounts.models import CustomUser
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=25, default="Unknown")
    charset = models.CharField(max_length=25, default="Unknown", help_text="The alphabet used by the language. Currently unused")
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="The genre(s) of the game.")
    description = models.CharField(max_length=200, blank="True", null="True")

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=1000)
    publisher_image = models.ImageField(upload_to='images/', null=True, blank=True)
    publisher_country = models.CharField(max_length=500)
    publisher_description = models.CharField(max_length=1000)
    def __str__(self):
        return self.publisher_name

class Developer(models.Model):
    developer_name = models.CharField(max_length=1000)
    developer_image = models.ImageField(upload_to='images/', blank=True, null=True)
    developer_country = models.CharField(max_length=500)
    developer_description = models.CharField(max_length=1000)
    def __str__(self):
        return self.developer_name

class Platform(models.Model):
    platform_name = models.CharField(max_length=25)
    platform_image = models.ImageField(upload_to='images/', blank=True, null=True)
    platform_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.platform_name


class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)

    developer = models.ForeignKey('Developer', on_delete=models.RESTRICT, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT, null=True)
    platform = models.ForeignKey('Platform', on_delete=models.RESTRICT, null=True)

    language = models.ManyToManyField(Language, related_name='language')
    genre = models.ManyToManyField(Genre, related_name='language')

    UNRATED = 'UR'
    EVERYONE = 'EO'
    EVERYONEPLUS = 'E+'
    TEEN = 'TE'
    MATURE = 'MA'
    ADULT = 'AO'

    RATING_LEVELS = [
        (UNRATED, 'Unrated'),
        (EVERYONE, 'Everyone'),
        (EVERYONEPLUS, 'Everyone 10+'),
        (TEEN, 'Teen'),
        (MATURE, 'Mature'),
        (ADULT, 'Adults Only')
    ]
    rating = models.CharField(
        max_length = 2,
        choices = RATING_LEVELS,
        default = UNRATED
    )

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['title', 'platform', 'release_date']

    def __str__(self):
        return self.title + ' (' + self.platform + ', ' + self.release_date.year + ')'

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000, help_text='Type in your review here')
    is_recommended = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.RESTRICT)



