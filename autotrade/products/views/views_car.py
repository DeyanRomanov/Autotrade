from cloudinary import uploader
from django.contrib.auth import mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import CurrentUserSaveProductMixin, OwnerAndPermStaffHaveCRUDPermissionMixin, \
    DeleteOnlyOwnersVehiclesAndDestroyImageMixin, OwnerCanNotEditReviewedProductsMixin, GetSuccessUrlAfterDeleteMixin
from autotrade.products.forms import CarCreateForm, CarEditForm
from autotrade.products.models import Car


class CarCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'cars/create_car.html'
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy('user vehicles')


class CarDetailsView(OwnerAndPermStaffHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Car
    template_name = 'cars/details_car.html'


class CarDeleteView(GetSuccessUrlAfterDeleteMixin, DeleteOnlyOwnersVehiclesAndDestroyImageMixin,
                    mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'cars/delete_car.html'
    model = Car


class CarEditView(OwnerCanNotEditReviewedProductsMixin,
                  OwnerAndPermStaffHaveCRUDPermissionMixin,
                  mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'cars/edit_car.html'
    model = Car
    form_class = CarEditForm

    def get_success_url(self):
        return reverse_lazy('details car', kwargs={'pk': self.object.pk})
