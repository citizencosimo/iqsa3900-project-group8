# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile_update_done')
    template_name = 'accounts/profile_update.html'

    def get_object(self, queryset=None):
        return self.request.user