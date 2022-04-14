from django import forms

from autotrade.products.models import Car, Vehicle, Motorcycle, Truck, Part
from common.mixins import FormControlWidgetMixin, CurrentUserSaveProductMixin


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


class CarCreateFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    motor = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Моля въведете кубатура на автомобила!'}))

    class Meta:
        model = Car
        exclude = (
            'user',
        )


class CarEditFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        exclude = (
            'user',
        )


class MotorcycleCreatFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        exclude = (
            'user',
        )


class MotorcycleEditFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        exclude = (
            'user',
        )


class TruckCreateFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, VehicleWidgets):
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


class TruckEditFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Truck
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'total_weight',
            'capacity',
            'category',
            'description',
        )


class PartCreateFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['name'].widget.attrs.update({'placeholder': 'Въведете има на продукта, пример: Врата'})
        self.fields['catalog_number'].widget.attrs.update(
            {'placeholder': 'Ако НЕ разполагате с каталожен номер на продукта оставете празно това поле'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Въведете допълнителна информация за продукта.\nПример:Ляв фар от Жигула 1986г. лява дирекция'})

    class Meta:
        model = Part
        exclude = (
            'user',
        )


class PartEditFormBase(CurrentUserSaveProductMixin, FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Part
        exclude = (
            'user',
        )


class CarEditForm(CarEditFormBase):
    pass


class CarCreateForm(CarCreateFormBase):
    pass


class MotorcycleCreatForm(MotorcycleCreatFormBase):
    pass


class MotorcycleEditForm(MotorcycleEditFormBase):
    pass


class TruckCreateForm(TruckCreateFormBase):
    pass


class TruckEditForm(TruckEditFormBase):
    pass


class PartCreateForm(PartCreateFormBase):
    pass


class PartEditForm(PartEditFormBase):
    pass


class AutotradeCarCreateForm(CarCreateFormBase):
    pass


class AutotradeTruckCreateForm(TruckCreateFormBase):
    pass


class AutotradeMotorcycleCreateForm(MotorcycleCreatFormBase):
    pass


class AutotradePartCreateForm(PartCreateFormBase):
    pass
