from django.contrib.auth import mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.models import Car, Motorcycle, Truck


class UserAdvertisementView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'user_advertisement.html'


class UserVehiclesView(mixins.LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = 'user_vehicles.html'

    def get_queryset(self):
        pk = self.request.user.pk
        cars = list(Car.objects.filter(user_id=pk))
        motorcycles = list(Motorcycle.objects.filter(user_id=pk))
        trucks = list(Truck.objects.filter(user_id=pk))
        vehicles_list = cars + motorcycles + trucks
        return vehicles_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        motorcycle_count = Motorcycle.objects.filter(user_id=pk).count()
        car_count = Car.objects.filter(user_id=pk).count()
        truck_count = Truck.objects.filter(user_id=pk).count()
        context['count'] = sum([
            motorcycle_count,
            car_count,
            truck_count,
        ])
        return context
