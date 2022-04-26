from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import OwnerAndPermStaffHaveCRUDPermissionMixin, CurrentUserSaveProductMixin, \
    DeleteOnlyOwnersVehiclesAndDestroyImageMixin, OwnerCanNotEditReviewedProductsMixin, GetSuccessUrlAfterDeleteMixin

from autotrade.products.forms import MotorcycleCreateForm, MotorcycleEditForm
from autotrade.products.models import Motorcycle


class MotorcycleCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'motorcycle/create_motorcycle.html'
    model = Motorcycle
    form_class = MotorcycleCreateForm
    success_url = reverse_lazy('user vehicles')


class MotorcycleDetailsView(OwnerAndPermStaffHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Motorcycle
    template_name = 'motorcycle/details_motorcycle.html'


class MotorcycleDeleteView(GetSuccessUrlAfterDeleteMixin, DeleteOnlyOwnersVehiclesAndDestroyImageMixin,
                           mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'motorcycle/delete_motorcycle.html'
    model = Motorcycle


class MotorcycleEditView(OwnerCanNotEditReviewedProductsMixin,
                         OwnerAndPermStaffHaveCRUDPermissionMixin,
                         mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'motorcycle/edit_motorcycle.html'
    model = Motorcycle
    form_class = MotorcycleEditForm

    def get_success_url(self):
        return reverse_lazy('details motorcycle', kwargs={'pk': self.object.pk})
