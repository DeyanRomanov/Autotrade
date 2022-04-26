from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

PRICE_DEFAULT_MESSAGE = 'В очакване на цена'
CRUD_USERS_PRODUCTS_PERMISSIONS = ['products.add_car', 'products.delete_car', 'products.view_car',
                                   'products.change_car',
                                   'products.add_truck', 'products.delete_truck', 'products.view_truck',
                                   'products.change_truck',
                                   'products.add_motorcycle', 'products.delete_motorcycle', 'products.view_motorcycle',
                                   'products.change_motorcycle',
                                   'products.add_part', 'products.delete_part', 'products.view_part',
                                   'products.change_part',
                                   ]

CRUD_PROFILE_USER_PERMISSIONS = ['userapp.view_profile',
                                 'userapp.change_profile',
                                 'userapp.delete_profile',
                                 'userapp.add_profile',
                                 ]


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
        if self.request.user.has_perms(CRUD_PROFILE_USER_PERMISSIONS):
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


class CurrentUserSaveProductMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OnlyOwnersCanAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.user == self.request.user and not self.request.user.has_perm('products.delete_car'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class GetSuccessUrlAfterDeleteMixin:
    def get_success_url(self):
        if self.request.user == self.object.user:
            return reverse_lazy('user vehicles')
        return reverse_lazy('advertisement to review')


class DeleteOnlyOwnersVehiclesAndDestroyImageMixin(OnlyOwnersCanAccessMixin):
    def save(self, commit=True):
        instance = self.__name__.objects.get(pk=self.object.pk)
        if commit:
            instance.image.storage.delete(instance.image.name)
            instance.delete()
        return reverse_lazy('user vehicles')


class OnlyStaffAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect(reverse_lazy('autotrade vehicles'))
        return super().dispatch(request, *args, **kwargs)


class UsersIsReviewedMixin:
    CHOICES_REVIEWED = [
        (False, 'Не'),
        (True, 'Да'),
    ]

    is_reviewed = models.BooleanField(
        choices=CHOICES_REVIEWED,
        default=CHOICES_REVIEWED[0][0],
        verbose_name='Разгледана',
    )


class OwnerCanNotEditReviewedProductsMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_reviewed and not self.request.user.has_perms(CRUD_USERS_PRODUCTS_PERMISSIONS):
            return redirect(reverse_lazy('user vehicles'))
        return super().dispatch(request, *args, **kwargs)


class OwnerAndPermStaffHaveCRUDPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        # Making sure that only owner or staff with perms can edit
        if obj.user == self.request.user or self.request.user.has_perms(CRUD_USERS_PRODUCTS_PERMISSIONS):
            return super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('user vehicles'))
