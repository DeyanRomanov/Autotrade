from django.contrib.auth import mixins
from django.core.paginator import Paginator

from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.cache import cache_page

from autotrade.products.forms import AutotradeCarCreateForm, AutotradeTruckCreateForm, AutotradeMotorcycleCreateForm, \
    AutotradePartCreateForm, AutotradeCarEditForm, AutotradeMotorcycleEditForm, AutotradeTruckEditForm, \
    AutotradePartEditForm
from autotrade.products.models import AutotradeCar, AutotradeMotorcycle, AutotradeTruck, AutotradePart, Car, Truck, \
    Motorcycle, Part
from autotrade.common.mixins import CurrentUserSaveProductMixin, OnlyStaffAccessMixin

PERMISSION_DENIED_MESSAGE = 'Нямате права за достъп'

_AUTOTRADE_PART_PERMISSION = ('products.add_autotradepart',
                              'products.delete_autotradepart',
                              'products.view_autotradepart',
                              'products.change_autotradepart',
                              )

_AUTOTRADE_CAR_PERMISSION = ('products.add_autotradecar',
                             'products.change_autotradecar',
                             'products.delete_autotradecar',
                             'products.view_autotradecar',
                             )

_AUTOTRADE_TRUCK_PERMISSION = ('products.add_autotradetruck',
                               'products.delete_autotradetruck',
                               'products.view_autotradetruck',
                               'products.change_autotradetruck',
                               )

_AUTOTRADE_MOTORCYCLE_PERMISSION = ('products.add_autotrademotorcycle',
                                    'products.delete_autotrademotorcycle',
                                    'products.view_autotrademotorcycle',
                                    'products.change_autotrademotorcycle',
                                    )

_AUTOTRADE_USER_PRODUCT_FULL_PERMISSION = (
    'products.add_car', 'products.delete_car', 'products.view_car', 'products.change_car',
    'products.add_truck', 'products.delete_truck', 'products.view_truck',
    'products.change_truck',
    'products.add_motorcycle', 'products.delete_motorcycle', 'products.view_motorcycle',
    'products.change_motorcycle',
    'products.add_part', 'products.delete_part', 'products.view_part', 'products.change_part',
)


class AutotradeCreateCarView(CurrentUserSaveProductMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    model = AutotradeCar
    form_class = AutotradeCarCreateForm
    template_name = 'autotrade/autotrade_create_car.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_CAR_PERMISSION


class AutotradeDetailsCarView(mixins.LoginRequiredMixin, generic.DetailView):
    model = AutotradeCar
    template_name = 'autotrade/autotrade_details_car.html'


class AutotradeEditCarView(mixins.PermissionRequiredMixin, generic.UpdateView):
    model = AutotradeCar
    form_class = AutotradeCarEditForm
    template_name = 'autotrade/autotrade_edit_car.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_CAR_PERMISSION


class AutotradeCreateTruckView(CurrentUserSaveProductMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    model = AutotradeTruck
    form_class = AutotradeTruckCreateForm
    template_name = 'autotrade/autotrade_create_truck.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_TRUCK_PERMISSION


class AutotradeDetailsTruckView(mixins.LoginRequiredMixin, generic.DetailView):
    model = AutotradeTruck
    template_name = 'autotrade/autotrade_details_truck.html'


class AutotradeEditTruckView(mixins.PermissionRequiredMixin, generic.UpdateView):
    model = AutotradeTruck
    form_class = AutotradeTruckEditForm
    template_name = 'autotrade/autotrade_edit_truck.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_TRUCK_PERMISSION


class AutotradeCreateMotorcycleView(CurrentUserSaveProductMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    model = AutotradeMotorcycle
    form_class = AutotradeMotorcycleCreateForm
    template_name = 'autotrade/autotrade_create_motorcycle.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_MOTORCYCLE_PERMISSION


class AutotradeDetailsMotorcycleView(mixins.LoginRequiredMixin, generic.DetailView):
    model = AutotradeMotorcycle
    template_name = 'autotrade/autotrade_details_motorcycle.html'


class AutotradeEditMotorcycleView(mixins.PermissionRequiredMixin, generic.UpdateView):
    model = AutotradeMotorcycle
    form_class = AutotradeMotorcycleEditForm
    template_name = 'autotrade/autotrade_edit_truck.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_MOTORCYCLE_PERMISSION


class AutotradeCreatePartView(CurrentUserSaveProductMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    model = AutotradePart
    form_class = AutotradePartCreateForm
    template_name = 'autotrade/autotrade_create_part.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_PART_PERMISSION


class AutotradeDetailsPartView(mixins.LoginRequiredMixin, generic.DetailView):
    model = AutotradePart
    template_name = 'autotrade/autotrade_details_part.html'


class AutotradeEditPartView(mixins.PermissionRequiredMixin, generic.UpdateView):
    model = AutotradePart
    form_class = AutotradePartEditForm
    template_name = 'autotrade/autotrade_edit_part.html'
    success_url = reverse_lazy('autotrade vehicles')
    permission_required = _AUTOTRADE_PART_PERMISSION


@cache_page(60*60*24*365)
class AutotradeVehicleCreateView(OnlyStaffAccessMixin, generic.TemplateView):
    template_name = 'autotrade/autotrade_create_vehicles.html'


class AutotradeVehicleView(generic.ListView):
    model = AutotradeCar
    template_name = 'autotrade/autotrade_vehicles.html'

    # paginator = Paginator(context)
    # current_page = request.GET.get('page', 1)

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
    template_name = 'autotrade/autotrade_reviewers_page.html'
    model = Car
    permission_required = _AUTOTRADE_USER_PRODUCT_FULL_PERMISSION
    permission_denied_message = PERMISSION_DENIED_MESSAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        vehicles = []
        context = super().get_context_data(**kwargs)
        vehicles.extend(list(Car.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Truck.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Motorcycle.objects.filter(is_reviewed=False)))
        vehicles.extend(list(Part.objects.filter(is_reviewed=False)))
        # sort by date of publication
        vehicles.sort(key=lambda x: x.date_of_publication)
        context['products'] = vehicles
        return context
