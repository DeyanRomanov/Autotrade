from django.contrib import admin

from autotrade.products.models import Car, Motorcycle, Truck, AutotradeCar, AutotradeTruck, AutotradeMotorcycle, Part, \
    AutotradePart


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
        'is_reviewed',
        'parts_category',
        'user',
    )


@admin.register(AutotradeCar)
class AutotradeCarAdmin(admin.ModelAdmin):
    model = AutotradeCar
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'description',
        'fuel',
        'motor',
    )


@admin.register(AutotradeTruck)
class AutotradeTruckAdmin(admin.ModelAdmin):
    model = AutotradeTruck
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'description',
        'total_weight',
        'capacity',
        'category',
    )


@admin.register(AutotradeMotorcycle)
class AutotradeMotorcycleAdmin(admin.ModelAdmin):
    model = AutotradeMotorcycle
    list_display = (
        'mark',
        'model',
        'image',
        'year',
        'price',
        'description',
        'motor_type',
        'cooling',
    )


@admin.register(AutotradePart)
class AutotradePartAdmin(admin.ModelAdmin):
    model = AutotradePart
    list_display = (
        'catalog_number',
        'condition',
        'image',
        'price',
        'parts_category',
        'user',
    )
