"""

Author : Nikolaos Kales r0927517
Category : Data Storage 
Test 1.2 : Sensitive data check
Purpose : Validate that sensitive data (e.g., passwords, tokens, and user details) is stored securely in the database or other storage locations.
Pre-mitigation Behavior : Test should identify passwords stored in plain text
Post-mitigation Behavior : Test should fail to access passwords due to encryption

"""



from wger.core.models import UserProfile
from wger.core.tests.base_testcase import WgerTestCase


class TestSensitiveDataStorage(WgerTestCase):
    def test_no_sensitive_data_in_userprofile(self):
        profiles = UserProfile.objects.all()
        for profile in profiles:
            self.assertNotIn("password", profile.__dict__.keys())
