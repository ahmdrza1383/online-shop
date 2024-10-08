from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = UserAdmin.list_display  # + ('age', 'phone_number')
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('age',)}),
    #     (None, {'fields': ('phone_number',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('age',)}),
    #     (None, {'fields': ('phone_number',)}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
