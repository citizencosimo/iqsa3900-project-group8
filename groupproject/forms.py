
from django.forms import ModelForm
from django import forms
from .models import Platform, Publisher, Developer, Game, Language, Genre, Image

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['publisher_name', 'publisher_country', 'publisher_description', 'publisher_image']

        widgets = {
            'publisher_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter publisher's name"
            }),
            'publisher_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter publisher's country"
            }),
            'publisher_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter a short description"
            }),
            'publisher_image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'image',
                'placeholder': "Select image",
            }),
        }

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['developer_name', 'developer_country', 'developer_description', 'developer_image']

        widgets = {
            'developer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter developer's name"
            }),
            'developer_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter developer's country"
            }),
            'developer_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter a short description"
            }),
            'developer_image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'image',
                'placeholder': "Select image",
            }),
        }

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['platform_name', 'platform_description', 'platform_image']

        widgets = {
            'platform_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter platform's name"
            }),
            'platform_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter platform's country"
            }),
            'platform_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter a short description"
            }),
            'platform_image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'image',
                'placeholder': "Select image",
            }),
        }

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
                'class': 'form-control',
                'id': 'image',
                'placeholder': "Select image",
            }),
        }

class LanguageForm(ModelForm):
    class Meta:
        model=Language
        fields='__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter language name"
            }),
            'charset': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter alphabet used"
            }),
        }

class GenreForm(ModelForm):
    class Meta:
        model=Genre
        fields='__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter genre name"
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter a short description"
            }),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image',)

