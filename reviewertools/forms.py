
from django.forms import ModelForm, widgets
from django.utils.safestring import mark_safe

from .models import ReviewTicket, Review
from django import forms


# class ThumbsUpDown(widgets.Widget):
#     template_name = 'group3900/templates/review/view.html'
#     def render(self, name, value, attrs=None, renderer=None):
#         if value is None:
#             value = ''
#         if value == 'thumbs-up':
#             icon_class = 'fa fa-thumbs-up'
#         elif value == 'thumbs-down':
#             icon_class = 'fa fa-thumbs-down'
#         else:
#             icon_class = ''
#         return mark_safe(
#             '<i class="%s"></i>' % icon_class
#         ) + super().render(name, value, attrs)
#     def value_from_datadict(self, data, files, name):
#         value= data.get(name)
#         if value in ('thumbs-up', 'thumbs-down'):
#             return value
#         return ''



class ReviewForm(ModelForm):

    class Meta:
        model=Review
        fields = ['description', 'comment', 'is_recommended']

class ReviewTicketForm(ModelForm):

    class Meta:
        model=ReviewTicket
        fields= ['reason', 'moderation_note']

class TicketResolutionForm(forms.Form):

    outcome = forms.BooleanField(label="Remove review?", required=False)
    ban_user = forms.BooleanField(label="Ban User?", required=False)
    message_to_creator = forms.CharField(label="Message to be sent to the author of this review:")



