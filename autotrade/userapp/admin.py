from django.contrib import admin

from autotrade.userapp.models import UserAppModel, Profile


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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'date_of_birth',
    )

    list_filter = (
        'first_name',
        'last_name',
        'date_of_birth',
    )

    ordering = (
        'first_name',
        'last_name',
        'date_of_birth',
    )
