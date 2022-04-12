from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from autotrade.products.forms import PartCreateForm, PartEditForm
from autotrade.products.models import Part


class PartCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'part/create_part.html'
    form_class = PartCreateForm
    success_url = reverse_lazy('user vehicles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PartDetailsView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Part
    template_name = 'part/details_part.html'


class PartDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'part/delete_part.html'
    success_url = reverse_lazy('user vehicles')
    model = Part


class PartEditView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'part/edit_part.html'
    form_class = PartEditForm
    success_url = reverse_lazy('user vehicles')
