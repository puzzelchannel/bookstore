from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class SignUpPageTests(TestCase):
    username = 'testing_user_username'
    email = 'testing_user_email'

    def test_signup_url(self):
        response = self.client.post('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_by_name(self):
        response = self.client.post(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
