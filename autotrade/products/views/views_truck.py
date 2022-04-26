from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import CurrentUserSaveProductMixin, OwnerAndPermStaffHaveCRUDPermissionMixin, \
    DeleteOnlyOwnersVehiclesAndDestroyImageMixin, OwnerCanNotEditReviewedProductsMixin, GetSuccessUrlAfterDeleteMixin

from autotrade.products.forms import TruckCreateForm, TruckEditForm
from autotrade.products.models import Truck


class TruckCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'truck/create_truck.html'
    model = Truck
    form_class = TruckCreateForm
    success_url = reverse_lazy('user vehicles')


class TruckDetailsView(OwnerAndPermStaffHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Truck
    template_name = 'truck/details_truck.html'


class TruckDeleteView(GetSuccessUrlAfterDeleteMixin, DeleteOnlyOwnersVehiclesAndDestroyImageMixin,
                      mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'truck/delete_truck.html'
    success_url = reverse_lazy('user vehicles')
    model = Truck


class TruckEditView(OwnerCanNotEditReviewedProductsMixin, OwnerAndPermStaffHaveCRUDPermissionMixin,
                    mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'truck/edit_truck.html'
    model = Truck
    form_class = TruckEditForm

    def get_success_url(self):
        return reverse_lazy('details truck', kwargs={'pk': self.object.pk})
