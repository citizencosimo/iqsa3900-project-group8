from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.ReviewIndexTest, name='review_index')
]
