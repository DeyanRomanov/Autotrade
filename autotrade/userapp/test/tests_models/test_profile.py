from django.test import TestCase

from autotrade.userapp.models import UserAppModel, Profile
from django.core.validators import ValidationError


class ProfileTest(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Deyan',
        'last_name': 'Romanov',
        'date_of_birth': '1987-06-21',
    }

    VALID_USER_DATA = {
        'email': 'deyan.romanov@gmail.com',
        'phone_number': '0888554455',
    }

    def test_profile_first_name_contains_symbol_not_letter__not_success(self):
        profile = Profile(
            first_name='Deyan@',
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_first_name_contains_space__not_success(self):
        profile = Profile(
            first_name='Deya n',
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_first_name_contains_number_letter__not_success(self):
        profile = Profile(
            first_name='1Deyan',
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_first_name_contains_only_letters__success(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        user = UserAppModel(**self.VALID_USER_DATA)
        user.save()
        profile.user = user
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_last_name_contains_symbbol_not_letter__not_success(self):
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name='Roman$ov',
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_last_name_contains_space__not_success(self):
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=' Romanov',
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_last_name_contains_number_letter__not_success(self):
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name='Roma1nov',
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
        )

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)

    def test_profile_last_name_contains_only_letters__success(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        user = UserAppModel(**self.VALID_USER_DATA)
        user.save()
        profile.user = user
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_get_gull_name(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        self.assertEqual('Deyan Romanov', profile.get_full_name)

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(ex.exception)
