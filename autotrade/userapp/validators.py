from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letter(value):
    if not value.isalpha():
        raise ValidationError('Names must contains only letters!')


@deconstructible
class ValidateEighteenYears:
    __DATE_TODAY = datetime.today().date()
    __ERROR_MESSAGE_MIN_YEARS = 'За да продължите, трябва да сте пълнолетен!'

    def __init__(self, min_years):
        self.min_years = min_years

    def __call__(self, value):
        current_years = (self.__DATE_TODAY - value).days / 365.25
        if current_years < self.min_years:
            raise ValidationError(f'{self.__ERROR_MESSAGE_MIN_YEARS}')
