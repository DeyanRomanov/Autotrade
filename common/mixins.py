from django import forms


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
