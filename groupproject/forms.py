
from django.forms import ModelForm
from django import forms
from .models import Platform, Publisher, Developer, Game, Language, Genre

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['publisher_name', 'publisher_country', 'publisher_description', 'publisher_image']
class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['developer_name', 'developer_country', 'developer_description', 'developer_image']

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['platform_name', 'platform_description', 'platform_image']

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'publisher', 'developer', 'release_date', 'platform',
                  'rating', 'genre', 'language', 'image']

        widgets = {
            'release_date': forms.widgets.DateInput(attrs={'type':'date'})
        }

class LanguageForm(ModelForm):
    class Meta:
        model=Language
        fields='__all__'

class GenreForm(ModelForm):
    class Meta:
        model=Genre
        fields='__all__'

