from django import forms
from .models import Publisher, Developer


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('publisher_name', 'publisher_image',
                  'publisher_country', 'publisher_description')


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('developer_name', 'developer_image',
                  'developer_country', 'developer_description')
