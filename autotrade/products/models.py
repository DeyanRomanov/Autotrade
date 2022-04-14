from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from autotrade.products.validators import MaxFileSizeInMbValidator, validate_future_date

UserModel = get_user_model()


def _get_max_choices_length(value):
    max_length = max([len(x[0]) for x in value])
    return max_length


class Vehicle(models.Model):
    MAX_MARK_LENGTH = 30
    MIN_MARK_LENGTH = 2

    MAX_MODEL_LENGTH = 30
    MIN_MODEL_LENGTH = 2

    PRICE_DEFAULT_MESSAGE = 'В очакване на цена'
    PRICE_MAX_LENGTH = len(PRICE_DEFAULT_MESSAGE)

    IMAGE_MAXSIZE_IN_MB = 2

    mark = models.CharField(
        max_length=MAX_MARK_LENGTH,
        validators=(
            MinLengthValidator(MIN_MARK_LENGTH),
        ),
        verbose_name='Марка',
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        verbose_name='Модел',
    )

    image = models.ImageField(
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAXSIZE_IN_MB),
        ),
        verbose_name='Изберете снимка до 2мб',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    year = models.DateField(
        validators=(
            validate_future_date,
        ),
        verbose_name='Година на производство',
    )

    price = models.CharField(
        max_length=PRICE_MAX_LENGTH,
        default=PRICE_DEFAULT_MESSAGE,
    )

    is_reviewed = models.BooleanField(
        default=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return f'{self.mark} {self.model} {self.__class__.__name__}'


class CarBase(Vehicle):
    PETROL = 'Дизел'
    GASOLINE = 'Бензин'
    ELECTRICITY = 'Електрически'
    HYBRID = 'Хибрид'
    GAS = 'Газ'
    CHOICES_FUEL = [
        (PETROL, PETROL),
        (GASOLINE, GASOLINE),
        (ELECTRICITY, ELECTRICITY),
        (HYBRID, HYBRID),
        (GAS, GAS),
    ]
    MAX_CHOICES_FUEL_LENGTH = _get_max_choices_length(CHOICES_FUEL)

    MOTOR_MIN_CAPACITY = 800
    MOTOR_MAX_CAPACITY = 7000

    fuel = models.CharField(
        max_length=MAX_CHOICES_FUEL_LENGTH,
        choices=CHOICES_FUEL,
        verbose_name='Гориво',
    )

    motor = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(MOTOR_MAX_CAPACITY),
            MinValueValidator(MOTOR_MIN_CAPACITY),
        ),
        verbose_name='Обем на двигател',
    )

    class Meta:
        abstract = True


class MotorcycleBase(Vehicle):
    AIR_COOLING = 'Въздушно'
    WATER_COOLING = 'Водно'
    CHOICES_COOLING = [
        (AIR_COOLING, AIR_COOLING),
        (WATER_COOLING, WATER_COOLING),
    ]
    COOLING_MAX_LENGTH = _get_max_choices_length(CHOICES_COOLING)

    CROSS = 'Кросов'
    SPORTS = 'Пистов'
    CHOPPER = 'Чопър'
    CHOICE_TYPE = [
        (CROSS, CROSS),
        (SPORTS, SPORTS),
        (CHOPPER, CHOPPER),
    ]
    TYPE_MAX_LENGTH = _get_max_choices_length(CHOICE_TYPE)

    motor_type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=CHOICE_TYPE,
        null=True,
        blank=True,
        verbose_name='Тип на мотора (незадължително поле)'
    )

    cooling = models.CharField(
        max_length=COOLING_MAX_LENGTH,
        choices=CHOICES_COOLING,
        null=True,
        blank=True,
        verbose_name='Вид охлаждане (незадължително поле)'
    )

    class Meta:
        abstract = True


class TruckBase(Vehicle):
    MIN_TOTAL_WEIGHT = 0

    MIN_CAPACITY = 0

    VAN = 'Ван'
    SPECIAL = 'Специален'
    CONSTRUCTION = 'Строителна техника'
    CATEGORY_CHOICES = [
        (VAN, VAN),
        (SPECIAL, SPECIAL),
        (CONSTRUCTION, CONSTRUCTION),
    ]
    MAX_CATEGORY_LENGTH = _get_max_choices_length(CATEGORY_CHOICES)

    total_weight = models.FloatField(
        validators=(
            MinValueValidator(MIN_TOTAL_WEIGHT),
        ),
        verbose_name='Общо тегло'
    )

    capacity = models.FloatField(
        validators=(
            MinValueValidator(MIN_TOTAL_WEIGHT),
        ),
        verbose_name='Товароносимост'
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        verbose_name='Категория'
    )

    class Meta:
        abstract = True


class PartBase(models.Model):
    MOTOR = 'Двигател'
    TRANSMISSION = 'Скорости'
    COUPE = 'КУПЕ'
    OTHERS = 'Други'
    PARTS_CHOICES = [
        (MOTOR, MOTOR),
        (TRANSMISSION, TRANSMISSION),
        (COUPE, COUPE),
        (OTHERS, OTHERS),
    ]
    MAX_PARTS_LENGTH = _get_max_choices_length(PARTS_CHOICES)

    NEW = 'Ново'
    USED = 'Използвано'
    UNPACKED = 'Разопаковано'
    CONDITION_CHOISES = [
        (NEW, NEW),
        (USED, USED),
        (UNPACKED, UNPACKED),
    ]
    MAX_CONDITION_LENGTH = _get_max_choices_length(CONDITION_CHOISES)

    MAX_CATALOG_CODE_LENGTH = 25

    MAX_NAME_LENGTH = 33

    MIN_PRICE = 1

    IMAGE_MAXSIZE_IN_MB = 1

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Наименование',
    )
    parts_category = models.CharField(
        max_length=MAX_PARTS_LENGTH,
        choices=PARTS_CHOICES,
        verbose_name="Категория"
    )

    condition = models.CharField(
        max_length=MAX_CONDITION_LENGTH,
        choices=CONDITION_CHOISES,
        verbose_name='Състояние',
    )

    catalog_number = models.CharField(
        max_length=MAX_CATALOG_CODE_LENGTH,
        null=True,
        blank=True,
        verbose_name='Каталожен номер'
    )

    price = models.IntegerField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
        verbose_name='Цена'
    )

    image = models.ImageField(
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAXSIZE_IN_MB),
        ),
        verbose_name='Изберете снимка до 1мб',
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class Car(CarBase):
    pass


class Motorcycle(MotorcycleBase):
    pass


class Truck(TruckBase):
    pass


class Part(PartBase):
    pass


class AutotradeMotorcycle(MotorcycleBase):
    pass


class AutotradeCar(CarBase):
    pass


class AutotradeTruck(TruckBase):
    pass


class AutotradePart(PartBase):
    pass
