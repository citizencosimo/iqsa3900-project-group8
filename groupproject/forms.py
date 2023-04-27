
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
                  'description', 'rating', 'genre', 'language', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter game title'
            }),
            'publisher': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Select publisher's name"
            }),
            'developer': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Select developer's name"
            }),
            'release_date': forms.DateInput(attrs={
                'id': 'release_date',
                'class': 'form-control',
                'placeholder': "Enter release date (mm/dd/yyyy)",
            }),
            'platform': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Select platform",
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Enter a brief description of the game",
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Select game rating",
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': "Select game genre",
            }),
            'language': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': "Select language",
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'placeholder': "Select image",
            }),
            #'release_date': forms.DateTimeInput(attrs={
            #    'class': 'form-control datetimepicker-input',
            #    'data-target': '#datetimepicker1'
            #})
            #'release_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class LanguageForm(ModelForm):
    class Meta:
        model=Language
        fields='__all__'

class GenreForm(ModelForm):
    class Meta:
        model=Genre
        fields='__all__'

