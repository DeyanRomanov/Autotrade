from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import OnlyOwnerHaveCRUDPermissionMixin, CurrentUserSaveProductMixin
from autotrade.products.forms import MotorcycleCreateForm, MotorcycleEditForm
from autotrade.products.models import Motorcycle


class MotorcycleCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'motorcycle/create_motorcycle.html'
    form_class = MotorcycleCreateForm
    success_url = reverse_lazy('user vehicles')


class MotorcycleDetailsView(OnlyOwnerHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Motorcycle
    template_name = 'motorcycle/details_motorcycle.html'


class MotorcycleDeleteView(OnlyOwnerHaveCRUDPermissionMixin, mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'motorcycle/delete_motorcycle.html'
    success_url = reverse_lazy('user vehicles')
    model = Motorcycle


class MotorcycleEditView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'motorcycle/edit_motorcycle.html'
    form_class = MotorcycleEditForm
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        return super().form_valid(form)