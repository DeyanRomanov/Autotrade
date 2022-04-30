from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class RegisterUserViewTest(TestCase):
    VALID_USER_DATA = {
        'email': 'abv@abv.bg',
        'password': 'Qqwe1123',
        'phone_number': '0886554455',
    }

    def test_if_all_correct_create_user(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        user = UserModel.objects.get()
        self.client.post(reverse('home'), data=self.VALID_USER_DATA)
        self.assertIsNotNone(user)
        self.assertEqual(self.VALID_USER_DATA['email'], user.email)

    def test_redirect_after_success_register_to_home(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse('home'))
        expected_url = "index.html"
        self.assertTemplateUsed(response, expected_url)

    def test_when_two_user_created_expect_to_contain_two_profiles(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        UserModel.objects.create_user(email='ffk@abv.bg', password='Qqwe1123')
        users = UserModel.objects.all()
        self.assertEqual(len(users), 2)

    def test_one_of_two_users_not_valid_data_expect_contain_one_profile(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        UserModel.objects.create_user(email='ffkabv.bg', password='Qqwe1123')
        users = UserModel.objects.all()
        self.assertEqual(len(users), 1)

