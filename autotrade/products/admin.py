from django.contrib import admin

from autotrade.products.models import Car, Motorcycle, Truck, AutotradeCar, AutotradeTruck, AutotradeMotorcycle, Part


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
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
class MotorcycleAdmin(admin.ModelAdmin):
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
class TruckAdmin(admin.ModelAdmin):
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


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = (
        'catalog_number',
        'condition',
        'image',
        'price',
        'parts_category',
        'user',
    )


@admin.register(AutotradeCar)
class AutotradeCarAdmin(admin.ModelAdmin):
    model = AutotradeCar


@admin.register(AutotradeTruck)
class AutotradeCarAdmin(admin.ModelAdmin):
    model = AutotradeTruck


@admin.register(AutotradeMotorcycle)
class AutotradeCarAdmin(admin.ModelAdmin):
    model = AutotradeMotorcycle
