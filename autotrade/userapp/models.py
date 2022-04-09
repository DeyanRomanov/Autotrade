from django.contrib.auth import models as auth_model
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from autotrade.userapp.managers import UserManager

from autotrade.userapp.validators import validate_only_letter, ValidateEighteenYears


class UserAppModel(auth_model.AbstractBaseUser, auth_model.PermissionsMixin):
    INVALID_PHONE_NUMBER_ERROR_MESSAGE = 'Моля въведете валиден номер във формат 0888112233'
    REGEX_VALIDATE_PHONE_NUMBER_BG = r'^08[7-9][5-9][0-9]{6}$'
    REGEX_CODE_MESSAGE = INVALID_PHONE_NUMBER_ERROR_MESSAGE
    MAX_PHONE_NUMBER = 10

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    phone_number = models.CharField(
        unique=True,
        max_length=MAX_PHONE_NUMBER,
        validators=(
            RegexValidator(regex=REGEX_VALIDATE_PHONE_NUMBER_BG,
                           message=INVALID_PHONE_NUMBER_ERROR_MESSAGE,
                           ),
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email} - {self.phone_number}'


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 35

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35

    MIN_YEARS_TO_ACCESS = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letter,
        ),
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letter,
        ),
        verbose_name='Last Name'
    )

    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
        validators=(
            ValidateEighteenYears(MIN_YEARS_TO_ACCESS),
        ),
    )

    user = models.OneToOneField(
        UserAppModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name}'
