from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase): 
    def test_create_user_successful(self):
        email = 'paulormartins12@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

