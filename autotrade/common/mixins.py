from django import forms
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

PRICE_DEFAULT_MESSAGE = 'В очакване на цена'


class FormControlWidgetMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class UserPermissionAccessMixin:
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CurrentUserSaveProductMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OnlyStaffAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect(reverse_lazy('autotrade vehicles'))
        return super().dispatch(request, *args, **kwargs)


class UsersIsReviewedMixin:
    is_reviewed = models.BooleanField(default=False, )


class UserFormPriceReviewedFieldsMixin:
    price = forms.CharField(widget=forms.HiddenInput(), initial=PRICE_DEFAULT_MESSAGE)
    is_reviewed = forms.CharField(widget=forms.HiddenInput(), initial=False)


class OnlyOwnerHaveCRUDPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        # Making sure that only owner can edit
        obj = self.get_object()
        if not obj.user == self.request.user:
            return redirect(reverse_lazy('user vehicles'))
        return super().dispatch(request, *args, **kwargs)

# here make if staff with perm must see price and reviewed
# class UsersCanNotEditPrice:
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         form.fields['price'].widget = forms.HiddenInput()
#         form.fields['is_reviewed'].widget = forms.HiddenInput()
#         return form