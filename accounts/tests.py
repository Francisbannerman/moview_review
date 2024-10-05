from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CustomUser

class CustomUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            email="test_user@email.com",
            password="testpassword"
        )

    def test_user_model(self):
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.email, "test_user@email.com")
        self.assertTrue(self.user.is_active)

        

