from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.ReviewIndexTest, name='review_index'),
    path('write_review/<int:game_id>', views.CreateReview, name='write_review')
]
