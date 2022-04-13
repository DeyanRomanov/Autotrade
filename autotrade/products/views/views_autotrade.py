from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import AutotradeCarCreateForm
from autotrade.products.models import AutotradeCar, Car, Part, Truck, Motorcycle

UserModel = get_user_model()


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
    staff = list(UserModel.objects.filter(is_staff=True).all())
    cars = []

    def get_queryset(self):
        cars = super().get_queryset().filter(user__in=self.staff)
        return cars

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        motorcycles = Motorcycle.objects.filter(user__in=self.staff).all()
        trucks = Truck.objects.filter(user__in=self.staff).all()
        parts = Part.objects.filter(user__in=self.staff).all()

        context['trucks'] = trucks
        context['motorcycles'] = motorcycles
        context['parts'] = parts
        context['cars'] = self.cars
        return context
