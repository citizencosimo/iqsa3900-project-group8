from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.ReviewIndexTest, name='review_index'),
    path('write_review/<int:game_id>', views.CreateReview, name='write_review'),
    path('update_review/<uuid:review_id>', views.UpdateReview, name='update_review'),
    path('report/<uuid:review_id>,', views.ReportReview, name='report_review'),
]
