from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .forms import UserProfileForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


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
    
    def form_valid(self, form):
        form.save(commit=False)
        if 'user_image' in self.request.FILES:
            self.object.user_image = self.request.FILES['user_image']
        self.object.save()
        return super().form_valid(form)
    
def profile_user(request):
    form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile_user.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile_update')
        else:
            messages.error(request, 'Please correct the error below.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/profile_change_password.html', {'form': form})
