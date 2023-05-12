from accounts.models import CustomUser
from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(
        max_length=25,
        # default="Unknown",
    )

    charset = models.CharField(
        max_length=100,
        # default="Unknown",
        # help_text="The alphabet used by the language. Currently unused",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language_view', args=str(self.pk))

class Genre(models.Model):
    name = models.CharField(
        max_length=25,
        #help_text="The genre(s) of the game.",
    )
    description = models.CharField(max_length=500, blank="True", null="True")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_view', args=str(self.pk))


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=1000)
    publisher_image = models.ImageField(
        upload_to='images/', null=True, blank=True)
    publisher_country = models.CharField(max_length=500)
    publisher_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.publisher_name
    def get_absolute_url(self):
        return reverse('publisher_view', args=str(self.pk))


class Developer(models.Model):
    developer_name = models.CharField(max_length=1000)
    developer_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    developer_country = models.CharField(max_length=500)
    developer_description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('developer_view', args=str(self.pk))


    def __str__(self):
        return self.developer_name


class Platform(models.Model):
    platform_name = models.CharField(max_length=25)
    platform_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    platform_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.platform_name
    def get_absolute_url(self):
        return reverse('platform_view', args=str(self.pk))

class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)

    developer = models.ForeignKey(
        'Developer', on_delete=models.RESTRICT, null=True)
    publisher = models.ForeignKey(
        'Publisher', on_delete=models.RESTRICT, null=True)
    platform = models.ForeignKey(
        'Platform', on_delete=models.RESTRICT, null=True)

    language = models.ManyToManyField(Language, related_name='language')
    genre = models.ManyToManyField(Genre, related_name='genre')

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
        max_length=2,
        choices=RATING_LEVELS,
        default=UNRATED
    )

    description = models.TextField(
        max_length=1000)

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['title', 'platform', 'release_date']

    def __str__(self):
        return self.title + ' (' + self.platform.platform_name + ', ' + str(self.release_date.year) + ')'
    def get_absolute_url(self):
        return reverse('game_view', args=str(self.pk))



