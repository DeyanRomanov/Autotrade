from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import OwnerAndPermStaffHaveCRUDPermissionMixin
from autotrade.products.forms import CarStaffEditForm, MotorcycleStaffEditForm, TruckStaffEditForm, PartStaffEditForm
from autotrade.products.models import Car, Motorcycle, Truck, Part


class CarStaffEditView(OwnerAndPermStaffHaveCRUDPermissionMixin,
                       generic.UpdateView):
    template_name = 'reviewers/staff_review_car.html'
    model = Car
    form_class = CarStaffEditForm
    success_url = reverse_lazy('advertisement to review')


class MotorcycleStaffEditView(OwnerAndPermStaffHaveCRUDPermissionMixin,
                              generic.UpdateView):
    template_name = 'reviewers/staff_review_motorcycle.html'
    model = Motorcycle
    form_class = MotorcycleStaffEditForm
    success_url = reverse_lazy('advertisement to review')


class TruckStaffEditView(OwnerAndPermStaffHaveCRUDPermissionMixin,
                         generic.UpdateView):
    template_name = 'reviewers/staff_review_truck.html'
    model = Truck
    form_class = TruckStaffEditForm
    success_url = reverse_lazy('advertisement to review')


class PartStaffEditView(OwnerAndPermStaffHaveCRUDPermissionMixin,
                        generic.UpdateView):
    template_name = 'reviewers/staff_review_part.html'
    model = Part
    form_class = PartStaffEditForm
    success_url = reverse_lazy('advertisement to review')
