from django.contrib import admin

from autotrade.userapp.models import UserAppModel


@admin.register(UserAppModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone_number',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
        'password',
    )

    ordering = (
        'last_login',
        'email',
    )

    list_filter = (
        'is_staff',
        'last_login',
    )
