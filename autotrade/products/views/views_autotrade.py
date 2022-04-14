from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import AutotradeCarCreateForm, AutotradeTruckCreateForm, AutotradeMotorcycleCreateForm, \
    AutotradePartCreateForm
from autotrade.products.models import AutotradeCar, AutotradeMotorcycle, AutotradeTruck, AutotradePart
from common.mixins import CurrentUserSaveProductMixin


class AutotradeCreateCarView(CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeCar
    form_class = AutotradeCarCreateForm
    template_name = 'autotrade/autotrade_create_car.html'
    success_url = reverse_lazy('autotrade vehicles')

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreateTruckView(CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeTruck
    form_class = AutotradeTruckCreateForm
    template_name = 'autotrade/autotrade_create_truck.html'
    success_url = reverse_lazy('autotrade vehicles')

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreateMotorcycleView(CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeMotorcycle
    form_class = AutotradeMotorcycleCreateForm
    template_name = 'autotrade/autotrade_create_motorcycles.html'
    success_url = reverse_lazy('autotrade vehicles')

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreatePartsView(CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradePart
    form_class = AutotradePartCreateForm
    template_name = 'autotrade/autotrade_create_parts.html'
    success_url = reverse_lazy('autotrade vehicles')

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeAdvertisementView(generic.TemplateView):
    template_name = 'autotrade/autotrade_car_for_sale.html'


class AutotradeVehicleCreateView(generic.TemplateView):
    template_name = 'autotrade/autotrade_create_vehicles.html'


class AutotradeVehicleView(generic.ListView):
    model = AutotradeCar
    template_name = 'autotrade/autotrade_vehicles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = AutotradeCar.objects.all()
        motorcycles = AutotradeMotorcycle.objects.all()
        trucks = AutotradeTruck.objects.all()
        parts = AutotradePart.objects.all()

        context['trucks'] = trucks
        context['motorcycles'] = motorcycles
        context['parts'] = parts
        context['cars'] = cars
        return context
