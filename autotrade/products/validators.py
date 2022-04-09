from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

FUTURE_DATE_ERROR_MESSAGE = 'Please enter valid date!'


@deconstructible
class MaxFileSizeInMbValidator:
    __EXCEPTION_MESSAGE = 'Image size must be less than 2mb! You can resize it here https://picresize.com/'
    __MEGABYTES_TO_BYTES = 1024 * 1024

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__MEGABYTES_TO_BYTES * self.max_size:
            raise ValidationError(f'{self.__EXCEPTION_MESSAGE}')


def validate_future_date(value):
    today = datetime.today().date()
    if value > today:
        raise ValidationError(FUTURE_DATE_ERROR_MESSAGE)
