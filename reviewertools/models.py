import uuid

from accounts.models import CustomUser
from django.db import models
from django.urls import reverse
from django.db import models



class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey('groupproject.Game', on_delete=models.CASCADE)
    description = models.CharField(
        max_length=255, help_text='A descriptive headline for your review'
    )
    comment = models.CharField(
        max_length=5000, help_text='Type in your review here')
    created = models.TimeField(auto_now_add=True)
    is_recommended = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    moderation_message = models.CharField(
        max_length=100, null=True, blank=True)

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.RESTRICT)





    def __str__(self):
        return self.description

class ReviewTicket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    moderation_target = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True)
    moderation_user = models.ForeignKey('accounts.CustomUser', on_delete = models.SET_NULL, null=True)

    INNAPROPRIATE = 'INN'
    OFFTOPIC = 'OFF'
    DOXING = 'DOX'
    OTHER = 'OTH'

    REPORTING_REASON = {
        (INNAPROPRIATE, 'This review contains innapropriate language or content.'),
        (OFFTOPIC, 'This review is not about the game.'),
        (DOXING, 'This review contains identifying personal information of the reviewer or someone else.'),
        (OTHER, 'This review is being reported for another reason.')
    }
    reason = models.CharField(
        max_length=3,
        choices=REPORTING_REASON,
        default=INNAPROPRIATE
    )
    moderation_note = models.CharField(max_length=5000, help_text='If you selected other, please tell us why.')

    ticket_open = models.BooleanField(default=False)

# Create your models here.
