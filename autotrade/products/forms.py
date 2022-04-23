from django import forms

from autotrade.products.models import Vehicle, Car, Motorcycle, Truck, \
    Part, AutotradeCar, AutotradeTruck, AutotradeMotorcycle, AutotradePart
from autotrade.common.mixins import FormControlWidgetMixin, UserFormPriceReviewedFieldsMixin


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

    # price = forms.CharField(widget=forms.HiddenInput(), initial=Vehicle.PRICE_DEFAULT_MESSAGE)
    # is_reviewed = forms.CharField(widget=forms.HiddenInput(), initial=False)


class CarCreateFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    motor = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Моля въведете кубатура на автомобила!'}))

    class Meta:
        exclude = (
            'user',
        )


class CarEditFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'fuel',
            'motor',
            'price',
        )


class MotorcycleCreateFormBase(FormControlWidgetMixin, UserFormPriceReviewedFieldsMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        exclude = (
            'user',
        )


class MotorcycleEditFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'motor_type',
            'cooling',
        )


class TruckCreateFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['total_weight'].widget.attrs.update({'placeholder': 'Въведете общо тегло в тонаж'})
        self.fields['capacity'].widget.attrs.update({'placeholder': 'Въведете товароносимост в тонаж'})

    class Meta:
        exclude = (
            'user',
        )


class TruckEditFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
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


class PartCreateFormBase(FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['name'].widget.attrs.update({'placeholder': 'Въведете има на продукта, пример: Врата'})
        self.fields['catalog_number'].widget.attrs.update(
            {'placeholder': 'Ако НЕ разполагате с каталожен номер на продукта оставете празно това поле'})
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Въведете допълнителна информация за продукта.'
                               '\nПример:Ляв фар от Жигула 1986г. лява дирекция'
            })

    class Meta:
        exclude = (
            'user',
        )


class PartEditFormBase(FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        exclude = (
            'user',
        )


class CarEditForm(CarEditFormBase, UserFormPriceReviewedFieldsMixin):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(CarEditFormBase.Meta):
        model = Car


class CarCreateForm(CarCreateFormBase, UserFormPriceReviewedFieldsMixin):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(CarCreateFormBase.Meta):
        model = Car


class MotorcycleCreateForm(MotorcycleCreateFormBase, UserFormPriceReviewedFieldsMixin):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(MotorcycleCreateFormBase.Meta):
        model = Motorcycle


class MotorcycleEditForm(MotorcycleEditFormBase, UserFormPriceReviewedFieldsMixin):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(MotorcycleCreateFormBase.Meta):
        model = Motorcycle


class TruckCreateForm(UserFormPriceReviewedFieldsMixin, TruckCreateFormBase):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(TruckCreateFormBase.Meta):
        model = Truck


class TruckEditForm(TruckEditFormBase):
    class Meta(TruckCreateFormBase.Meta):
        model = Truck


class PartCreateForm(UserFormPriceReviewedFieldsMixin, PartCreateFormBase):
    price = UserFormPriceReviewedFieldsMixin.price
    is_reviewed = UserFormPriceReviewedFieldsMixin.is_reviewed

    class Meta(PartCreateFormBase.Meta):
        model = Part


class PartEditForm(PartEditFormBase):
    class Meta(PartCreateFormBase.Meta):
        model = Part


class AutotradeCarCreateForm(CarCreateFormBase):
    class Meta(CarCreateFormBase.Meta):
        model = AutotradeCar


class AutotradeCarEditForm(CarEditFormBase):
    class Meta(CarEditFormBase.Meta):
        model = AutotradeCar


class AutotradeTruckCreateForm(TruckCreateFormBase):
    class Meta(TruckCreateFormBase.Meta):
        model = AutotradeTruck


class AutotradeTruckEditForm(TruckEditFormBase):
    class Meta(TruckCreateFormBase.Meta):
        model = AutotradeTruck


class AutotradeMotorcycleCreateForm(MotorcycleCreateFormBase):
    class Meta(MotorcycleCreateFormBase.Meta):
        model = AutotradeMotorcycle


class AutotradePartCreateForm(PartCreateFormBase):
    class Meta(PartCreateFormBase.Meta):
        model = AutotradePart
