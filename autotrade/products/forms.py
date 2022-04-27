from django import forms

from autotrade.products.models import Car, Motorcycle, Truck, \
    Part, AutotradeCar, AutotradeTruck, AutotradeMotorcycle, AutotradePart
from autotrade.common.mixins import FormControlWidgetMixin, UsersIsReviewedMixin, CRUD_USERS_PRODUCTS_PERMISSIONS


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


class CarCreateFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    motor = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Моля въведете кубатура на автомобила!'}))

    class Meta:
        model = Car
        exclude = (
            'user',
        )


class CarEditFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'fuel',
            'motor',
        )


class CarStaffEditForm(CarEditFormBase):
    class Meta:
        model = Car
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'fuel',
            'motor',
            'price',
            'is_reviewed',
        )


class MotorcycleCreateFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        exclude = (
            'user',
        )


class MotorcycleEditFormBase(FormControlWidgetMixin, VehicleWidgets):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Motorcycle
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'motor_type',
            'cooling',
        )


class MotorcycleStaffEditForm(MotorcycleEditFormBase):
    class Meta:
        model = Motorcycle
        fields = (
            'image',
            'mark',
            'model',
            'year',
            'description',
            'motor_type',
            'cooling',
            'price',
            'is_reviewed',
        )


class TruckCreateFormBase(FormControlWidgetMixin, VehicleWidgets):
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


class TruckEditFormBase(FormControlWidgetMixin, VehicleWidgets):
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


class TruckStaffEditForm(TruckEditFormBase):
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
            'price',
            'is_reviewed',
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
        model = Part
        exclude = (
            'user',
        )


class PartEditFormBase(FormControlWidgetMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Part
        fields = (
            'name',
            'parts_category',
            'condition',
            'catalog_number',
            'description',
        )


class PartStaffEditForm(PartEditFormBase):
    class Meta:
        model = Part
        fields = (
            'name',
            'parts_category',
            'condition',
            'catalog_number',
            'description',
            'price',
            'is_reviewed',
        )


class CarCreateForm(UsersIsReviewedMixin, CarCreateFormBase):
    is_reviewed = UsersIsReviewedMixin.is_reviewed

    class Meta(CarCreateFormBase.Meta):
        model = Car
        widgets = {
            'price': forms.HiddenInput(),
            'is_reviewed': forms.HiddenInput(),
        }


class CarEditForm(UsersIsReviewedMixin, CarEditFormBase):
    class Meta(CarEditFormBase.Meta):
        model = Car


class MotorcycleCreateForm(UsersIsReviewedMixin, MotorcycleCreateFormBase):
    is_reviewed = UsersIsReviewedMixin.is_reviewed

    class Meta(MotorcycleCreateFormBase.Meta):
        model = Motorcycle
        widgets = {
            'price': forms.HiddenInput(),
            'is_reviewed': forms.HiddenInput(),
        }


class MotorcycleEditForm(UsersIsReviewedMixin, MotorcycleEditFormBase):
    class Meta(MotorcycleEditFormBase.Meta):
        model = Motorcycle


class TruckCreateForm(UsersIsReviewedMixin, TruckCreateFormBase):
    is_reviewed = UsersIsReviewedMixin.is_reviewed

    class Meta(TruckCreateFormBase.Meta):
        model = Truck
        widgets = {
            'price': forms.HiddenInput(),
            'is_reviewed': forms.HiddenInput(),
        }


class TruckEditForm(TruckEditFormBase):
    class Meta(TruckEditFormBase.Meta):
        model = Truck


class PartCreateForm(UsersIsReviewedMixin, PartCreateFormBase):
    is_reviewed = UsersIsReviewedMixin.is_reviewed

    class Meta(PartCreateFormBase.Meta):
        model = Part
        widgets = {
            'price': forms.HiddenInput(),
            'is_reviewed': forms.HiddenInput(),
        }


class PartEditForm(PartEditFormBase):
    class Meta(PartEditFormBase.Meta):
        model = Part


class AutotradeCarCreateForm(CarCreateFormBase):
    class Meta(CarCreateFormBase.Meta):
        model = AutotradeCar


class AutotradeCarEditForm(CarEditFormBase):
    class Meta(CarEditFormBase.Meta):
        model = AutotradeCar
        fields = '__all__'


class AutotradeTruckCreateForm(TruckCreateFormBase):
    class Meta(TruckCreateFormBase.Meta):
        model = AutotradeTruck


class AutotradeTruckEditForm(TruckEditFormBase):
    class Meta(TruckEditFormBase.Meta):
        model = AutotradeTruck


class AutotradeMotorcycleCreateForm(MotorcycleCreateFormBase):
    class Meta(MotorcycleCreateFormBase.Meta):
        model = AutotradeMotorcycle


class AutotradeMotorcycleEditForm(MotorcycleEditFormBase):
    class Meta(MotorcycleEditFormBase.Meta):
        model = AutotradeMotorcycle


class AutotradePartCreateForm(PartCreateFormBase):
    class Meta(PartCreateFormBase.Meta):
        model = AutotradePart


class AutotradePartEditForm(PartEditFormBase):
    class Meta(PartEditFormBase.Meta):
        model = AutotradePart
