from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import CurrentUserSaveProductMixin, OwnerAndPermStaffHaveCRUDPermissionMixin, \
    DeleteOnlyOwnersVehiclesAndDestroyImageMixin, OwnerCanNotEditReviewedProductsMixin, GetSuccessUrlAfterDeleteMixin
from autotrade.products.forms import PartCreateForm, PartEditForm
from autotrade.products.models import Part


class PartCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'part/create_part.html'
    model = Part
    form_class = PartCreateForm
    success_url = reverse_lazy('user vehicles')


class PartDetailsView(OwnerAndPermStaffHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Part
    template_name = 'part/details_part.html'


class PartDeleteView(GetSuccessUrlAfterDeleteMixin, DeleteOnlyOwnersVehiclesAndDestroyImageMixin,
                     mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'part/delete_part.html'
    success_url = reverse_lazy('user vehicles')
    model = Part


class PartEditView(OwnerCanNotEditReviewedProductsMixin, OwnerAndPermStaffHaveCRUDPermissionMixin,
                   mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'part/edit_part.html'
    model = Part
    form_class = PartEditForm

    def get_success_url(self):
        return reverse_lazy('details part', kwargs={'pk': self.object.pk})
