from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import AutotradeCarCreateForm
from autotrade.products.models import AutotradeCar, Car

UserApp = get_user_model()


class AutotradeCreateCarView(generic.CreateView):
    model = AutotradeCar
    form_class = AutotradeCarCreateForm
    template_name = 'autotrade/autotrade_create_car.html'
    success_url = reverse_lazy('autotrade vehicles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AutotradeAdvertisementView(generic.TemplateView):
    template_name = 'autotrade/autotrade_car_for_sale.html'


class AutotradeVehicleCreateView(generic.TemplateView):
    template_name = 'autotrade/autotrade_create_vehicles.html'


class AutotradeVehicleView(generic.ListView):
    model = Car
    template_name = 'autotrade/autotrade_vehicles.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=is_staff)
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     cars = []
    #     for staff in list(UserApp.objects.filter(is_staff=True)):
    #         cars.append(Car.objects.filter(user=staff).all())
    #     context['cars'] = cars
    #     context['trucks'] = trucks
    #     context['trucks'] = trucks
    #     context['trucks'] = trucks
    #     return context
