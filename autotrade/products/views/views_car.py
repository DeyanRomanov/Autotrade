from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import CurrentUserSaveProductMixin, OnlyOwnerHaveCRUDPermissionMixin
from autotrade.products.forms import CarCreateForm, CarEditForm
from autotrade.products.models import Car


class CarCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'cars/create_car.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('user vehicles')


class CarDetailsView(OnlyOwnerHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'cars/details_car.html'
    model = Car


class CarsDeleteView(OnlyOwnerHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'cars/delete_car.html'
    success_url = reverse_lazy('user vehicles')
    model = Car


class CarsEditView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'cars/edit_car.html'
    model = Car
    form_class = CarEditForm
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        return super().form_valid(form)
