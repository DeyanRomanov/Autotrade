from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import AutotradeCarCreateForm
from autotrade.products.models import AutotradeCar, AutotradeMotorcycle, AutotradeTruck

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
    model = AutotradeCar
    template_name = 'autotrade/autotrade_vehicles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        staff = list(UserModel.objects.filter(is_staff=True).all())
        context = super().get_context_data(**kwargs)
        cars = AutotradeCar.objects.filter(user__in=staff).all()
        motorcycles = AutotradeMotorcycle.objects.filter(user__in=staff).all()
        trucks = AutotradeTruck.objects.filter(user__in=staff).all()
        parts = Part.objects.filter(user__in=staff).all()

        context['trucks'] = trucks
        context['motorcycles'] = motorcycles
        context['parts'] = parts
        context['cars'] = cars
        return context
