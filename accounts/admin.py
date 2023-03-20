from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "username",]
    fieldsets = (
        (('User'),{'fields': ('email', 'first_name', 'last_name', 'password')}),
        (('Flags'),{'fields': ('is_superuser', 'is_staff', 'is_active')}),
        (('Moderation'),{'fields': ('is_onprobation', 'moderation_message')}),
        (('Groups'),{'fields': ['groups']})
    )

admin.site.register(CustomUser, CustomUserAdmin)
