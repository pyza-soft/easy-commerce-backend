from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'phone',
        'first_name',
        'last_name',
        'is_active',
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')}
        ),
        (
            _('Personal info'),
            {
                'fields': ('first_name', 'last_name', 'email', 'phone')
            }
        ),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }
        ),
        (
            _('Important dates'),
            {
                'fields': ('last_login', 'date_joined')
            }
        ),
    )
