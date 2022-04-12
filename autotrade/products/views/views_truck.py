from django.contrib.auth import mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import TruckCreateForm, TruckEditForm
from autotrade.products.models import Truck
from common.mixins import UserPermissionAccessMixin


class TruckCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    form_class = TruckCreateForm
    template_name = 'truck/create_truck.html'
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TruckDetailsView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Truck
    template_name = 'truck/details_truck.html'


class TruckEditView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'truck/edit_truck.html'
    model = Truck
    form_class = TruckEditForm

    success_url = reverse_lazy('user vehicles')

    def dispatch(self, request, *args, **kwargs):
        context = super().dispatch(request, *args, **kwargs)
        context['is_owner'] = self.request.user == self.object.user
        if not context['is_owner']:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class TruckDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'truck/delete_truck.html'
    success_url = reverse_lazy('user vehicles')
    model = Truck
