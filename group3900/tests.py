import os

from django.conf import settings
from django.test import TestCase
from password_strength import PasswordPolicy

class SecurityTests(TestCase):

    policy = PasswordPolicy.from_names(
        length = 8,
        entropybits = 30
    )
    def test_secret_key_strength(self):
        self.assertFalse(self.policy.test(os.environ.get('SECRET_KEY')))


