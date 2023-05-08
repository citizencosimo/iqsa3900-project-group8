from django.urls import path
from .views import ProfileUpdateView, SignUpView, profile_user
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', profile_user, name='profile_user'),
    path('profile/update/done/', auth_views.TemplateView.as_view(template_name='accounts/profile_update_done.html'), name='profile_update_done'),
    path('profile/password/', views.change_password, name='change_password'),   
]