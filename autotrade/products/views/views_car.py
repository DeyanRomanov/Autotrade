from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import CarCreateForm, CarEditForm
from autotrade.products.models import Car


class CarCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'cars/create_car.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarDetailsView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'cars/details_car.html'
    model = Car


class CarsDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'cars/delete_car.html'
    success_url = reverse_lazy('user vehicles')
    model = Car


class CarsEditView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'cars/edit_car.html'
    model = Car
    form_class = CarEditForm
    success_url = reverse_lazy('user vehicles')
