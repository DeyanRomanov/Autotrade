from autotrade.products.models import AutotradeCar, AutotradeTruck, AutotradeMotorcycle, AutotradePart


def last_viewed_vehicles(get_response):
    def middleware(request):
        last_viewed_vehicle = request.session.get('last_viewed_vehicle_pks', [])
        all_vehicles = []
        all_vehicles.extend(list(AutotradeCar.objects.filter(id__in=last_viewed_vehicle)))
        all_vehicles.extend(list(AutotradeTruck.objects.filter(id__in=last_viewed_vehicle)))
        all_vehicles.extend(list(AutotradeMotorcycle.objects.filter(id__in=last_viewed_vehicle)))
        all_vehicles.extend(list(AutotradePart.objects.filter(id__in=last_viewed_vehicle)))
        request.last_viewed_vehicle = all_vehicles
        return get_response(request)

    return middleware
