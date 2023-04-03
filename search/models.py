from django.db import models

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)