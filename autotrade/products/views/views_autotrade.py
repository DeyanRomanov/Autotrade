from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import AutotradeCarCreateForm, AutotradeTruckCreateForm, AutotradeMotorcycleCreateForm, \
    AutotradePartCreateForm, AutotradeCarEditForm
from autotrade.products.models import AutotradeCar, AutotradeMotorcycle, AutotradeTruck, AutotradePart, Car, Truck, \
    Motorcycle, Part
from autotrade.common.mixins import CurrentUserSaveProductMixin, OnlyStaffAccessMixin


class AutotradeCreateCarView(mixins.PermissionRequiredMixin, CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeCar
    form_class = AutotradeCarCreateForm
    template_name = 'autotrade/autotrade_create_car.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = ('products.add_autotradecar', )

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeDetailsCarView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'autotrade/autotrade_details_car.html'


class AutotradeEditCarView(mixins.PermissionRequiredMixin, CurrentUserSaveProductMixin, generic.UpdateView):
    model = AutotradeCar
    form_class = AutotradeCarEditForm
    template_name = 'autotrade/autotrade_edit_car.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = ('products.change_autotradecar', )

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreateTruckView(mixins.PermissionRequiredMixin, CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeTruck
    form_class = AutotradeTruckCreateForm
    template_name = 'autotrade/autotrade_create_truck.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = ('products.add_autotradetruck', )

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreateMotorcycleView(mixins.PermissionRequiredMixin, CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradeMotorcycle
    form_class = AutotradeMotorcycleCreateForm
    template_name = 'autotrade/autotrade_create_motorcycle.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = ('products.add_autotrademotorcycle', )

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeCreatePartView(mixins.PermissionRequiredMixin, CurrentUserSaveProductMixin, generic.CreateView):
    model = AutotradePart
    form_class = AutotradePartCreateForm
    template_name = 'autotrade/autotrade_create_part.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = ('products.add_autotradepart', )

    def form_valid(self, form):
        return super().form_valid(form)


class AutotradeVehicleCreateView(OnlyStaffAccessMixin, generic.TemplateView):
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


class AutotradeUsersProductView(mixins.PermissionRequiredMixin, generic.ListView):
    template_name = 'autotrade_reviewers_page.html'
    model = Car
    permission_required = ('products.add_car', 'products.delete_car', 'products.update_car', 'products.change_car',
                           'products.add_truck', 'products.delete_truck', 'products.update_truck', 'products.change_truck',
                           'products.add_motorcycle', 'products.delete_motorcycle', 'products.update_motorcycle', 'products.change_motorcycle',
                           'products.add_part', 'products.delete_part', 'products.update_part', 'products.change_part',
                           )

    def get_context_data(self, *, object_list=None, **kwargs):
        vehicles = []
        context = super().get_context_data(**kwargs)
        vehicles.extend(list(Car.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Truck.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Motorcycle.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Part.objects.filter(is_reviewed=False)))
        context['products'] = vehicles
        return context

    ordering = ('-date_of_publication',)
