from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.common.mixins import CurrentUserSaveProductMixin
from autotrade.products.forms import PartCreateForm, PartEditForm
from autotrade.products.models import Part


class PartCreateView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'part/create_part.html'
    form_class = PartCreateForm
    success_url = reverse_lazy('user vehicles')


class PartDetailsView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Part
    template_name = 'part/details_part.html'


class PartDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'part/delete_part.html'
    success_url = reverse_lazy('user vehicles')
    model = Part


class PartEditView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'part/edit_part.html'
    form_class = PartEditForm
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        return super().form_valid(form)
