from django.forms import ModelForm
from .models import ReviewTicket, Review
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields = ['description', 'comment', 'is_recommended']
