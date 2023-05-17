from django.shortcuts import redirect
from django.urls import reverse

class StaffRequiredMixin:
    def dispatch(self, request):
        print(request.user.is_staff)
        if not request.user.is_staff:
            return redirect('home')
        return None