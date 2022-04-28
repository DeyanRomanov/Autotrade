from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
UserModel = get_user_model()


class RegisterUserViewTest(TestCase):
    VALID_USER_DATA = {
        'email': 'abv@abv.bg',
        'password': 'Qqwe1123',
    }

    def test_if_all_correct_create_user(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        user = UserModel.objects.get()
        self.client.post(reverse('home'), data=self.VALID_USER_DATA)
        self.assertIsNotNone(user)
        self.assertEqual(self.VALID_USER_DATA['email'], user.email)

    # def test_redirect_after_success_register_to_home(self):
    #     UserModel.objects.create_user(**self.VALID_USER_DATA)
    #     expected_url = reverse('home')
    #     self.assertRedirects(response, expected_url)
