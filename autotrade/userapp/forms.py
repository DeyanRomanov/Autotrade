import os
from datetime import date

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.validators import MinLengthValidator, RegexValidator

from autotrade.products.models import Car, Motorcycle, Truck, Vehicle
from autotrade.userapp.models import Profile, UserAppModel
from autotrade.userapp.validators import validate_only_letter, ValidateEighteenYears

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    this_year = date.today().year - 17
    year_range = [x for x in range(this_year - 100, this_year)]

    phone_number = forms.CharField(
        max_length=UserAppModel.MAX_PHONE_NUMBER,
        validators=(
            RegexValidator(regex=UserAppModel.REGEX_VALIDATE_PHONE_NUMBER_BG,
                           message=UserAppModel.INVALID_PHONE_NUMBER_ERROR_MESSAGE,
                           ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

            """
            https://stackoverflow.com/questions/49413185/django-password-fields-placeholder
            The Meta.widgets option doesn't apply to fields that were declared in the form. 
            See the note in the docs. In this case, password1 and password2 are declare on the 
            UserCreationForm (they aren't model fields), therefore you can't use them in widgets.
            """

            if field == 'password1':
                self.fields[field].widget.attrs.update({'placeholder': 'Please enter your password'})
            elif field == 'password2':
                self.fields[field].widget.attrs.update({'placeholder': 'Please repeat your password'})
            elif field == 'phone_number':
                self.fields[field].widget.attrs.update({'placeholder': 'Please enter your phone number'})

    # profile fields
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your first name'}),
        validators=(validate_only_letter, MinLengthValidator(Profile.FIRST_NAME_MIN_LENGTH)),
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your last name'}),
        validators=(validate_only_letter, MinLengthValidator(Profile.LAST_NAME_MIN_LENGTH)),
    )

    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=year_range),
        validators=(ValidateEighteenYears(Profile.MIN_YEARS_TO_ACCESS),
                    ),
    )

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password1',
            'password2',
            'phone_number',
        )

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email address',
                },
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            profile.save()

        return user


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            'user',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            'user',
        )

        widgets = {
            'date_of_birth': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'disable': 'disable',
                },
            ),
        }


def delete_vehicles(instances):
    for inst in instances:
        inst.delete()
        # inst.__name__.image.storage.delete(inst.image.name)
    return instances


class ProfileDeleteForm(forms.ModelForm):
    def delete(self, using=None, keep_parents=False):
        cars = list(Car.objects.get(user_id=self.request.user.pk).all())
        delete_vehicles(cars)
        trucks = list(Truck.objects.get(user_id=self.request.user.pk).all())
        delete_vehicles(trucks)
        motorcycles = list(Motorcycle.objects.get(user_id=self.request.user.pk).all())
        delete_vehicles(motorcycles)
        super().delete()
        self.instance.delete()
        return self.instance()

    class Meta:
        model = Profile
        fields = '__all__'
