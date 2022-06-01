from django.contrib.auth import mixins
from django.views import generic

from autotrade.products.models import Car, Motorcycle, Truck, Part


class UserAdvertisementView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'user_advertisement.html'


class UserVehiclesView(mixins.LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = 'user_vehicles.html'

    # get advertisement only for current user
    def get_queryset(self):
        pk = self.request.user.pk
        cars = list(Car.objects.filter(user_id=pk))
        motorcycles = list(Motorcycle.objects.filter(user_id=pk))
        trucks = list(Truck.objects.filter(user_id=pk))
        parts = list(Part.objects.filter(user_id=pk))
        vehicles_list = cars + motorcycles + trucks + parts
        vehicles_list.sort(key=lambda x: -x.is_reviewed)
        return vehicles_list

    # take total advertisement count
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        motorcycle_count = Motorcycle.objects.filter(user_id=pk).count()
        car_count = Car.objects.filter(user_id=pk).count()
        truck_count = Truck.objects.filter(user_id=pk).count()
        part_count = Part.objects.filter(user_id=pk).count()
        context['count'] = sum([
            motorcycle_count,
            car_count,
            truck_count,
            part_count,
        ])
        return context

