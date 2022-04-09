from django.contrib import admin

from autotrade.products.models import Car, Motorcycle, Truck


@admin.register(Car)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'is_reviewed',
        'description',
        'fuel',
        'motor',
    )


@admin.register(Motorcycle)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'is_reviewed',
        'description',
        'motor_type',
        'cooling',
    )


@admin.register(Truck)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'is_reviewed',
        'description',
        'total_weight',
        'capacity',
        'category',
    )
