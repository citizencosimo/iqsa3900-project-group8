from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

class StaffRequiredMixin:
    def dispatch(self, request):
        if not request.user.is_staff:
            messages.error(request, "Unauthorized")
            return redirect('home')
        return None