from django import forms

from autotrade.products.models import Car, Vehicle, Motorcycle, Truck
from common.mixins import FormControlWidgetMixin


class VehicleWidgets(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mark'].widget.attrs.update({'placeholder': 'Въведете марка'})
        self.fields['model'].widget.attrs.update({'placeholder': 'Въведете модел'})
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Въведете описание на модела, екстри и забележки',
            'rows': '3',
        })

        self.fields['year'].widget.attrs.update({
            'placeholder': 'Въведете година на производство във формат гггг/мм/дд',
            'type': 'date',
        }, )

    price = forms.CharField(widget=forms.HiddenInput(), initial=Vehicle.PRICE_DEFAULT_MESSAGE)
    is_reviewed = forms.CharField(widget=forms.HiddenInput(), initial=False)


class CarCreateForm(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    motor = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Моля въведете кубатура на автомобила!'}))

    class Meta:
        model = Car
        exclude = (
            'user',
        )


class CarEditForm(FormControlWidgetMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        fields = '__all__'


class MotorcycleCreatForm(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        exclude = (
            'user',
        )


class MotorcycleEditForm(FormControlWidgetMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        fields = '__all__'


class TruckCreateForm(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['total_weight'].widget.attrs.update({'placeholder': 'Въведете общо тегло в тонаж'})
        self.fields['capacity'].widget.attrs.update({'placeholder': 'Въведете товароносимост в тонаж'})

    class Meta:
        model = Truck
        exclude = (
            'user',
        )


class TruckEditForm(FormControlWidgetMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Truck
        fields = '__all__'


class AutotradeCarCreateForm(CarCreateForm):
    pass

class AutotradeTruckCreateForm(TruckCreateForm):
    pass


class AutotradeMotorcycleCreateForm(MotorcycleCreatForm):
    pass
