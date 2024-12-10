"""

Author : Nikolaos Kales r0927517
Category : Data Storage 
Test 1.1 : Plain Text Credential Check
Purpose : Validate that sensitive data (e.g., passwords, tokens, and user details) is stored securely in the database or other storage locations.
Pre-mitigation Behavior : Test should identify passwords stored in plain text
Post-mitigation Behavior : Test should fail to access passwords due to encryption

"""
import os
from django.contrib.auth.hashers import identify_hasher
from django.contrib.auth.models import User
from wger.core.tests.base_testcase import WgerTestCase
from wger.core.models import Language



class TestPasswordStorage(WgerTestCase):
    def setUp(self):
        # Set the RECAPTCHA_TESTING environment variable
        os.environ['RECAPTCHA_TESTING'] = '1'

        # Ensure the core_language table has the required data
        Language.objects.get_or_create(
            short_name="en",
            defaults={
                "full_name": "English",
                "full_name_en": "English"
            }
        )

    def test_passwords_are_hashed(self):
        # Create a test user (if not already created in fixtures)
        User.objects.create_user(username="testuser", password="testpassword")
        
        # Fetch the user and check password hashing
        user = User.objects.get(username="testuser")
        self.assertIsNotNone(user.password, "Password field is empty.")
        try:
            identify_hasher(user.password)
        except ValueError:
            self.fail("Password is not hashed securely.")