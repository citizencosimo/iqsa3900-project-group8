from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    user_image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = CustomUser
        fields = ("user_image","username","first_name", "last_name", "email")

class CustomUserChangeForm(UserChangeForm):
    user_image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = CustomUser
        fields = ("user_image","username","first_name", "last_name", "email")