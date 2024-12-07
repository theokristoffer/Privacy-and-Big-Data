from wger.core.tests.base_testcase import WgerTestCase

class SimpleTestCase(WgerTestCase):
    """
    A simple test case to verify that the homepage redirects correctly.
    """

    def test_homepage_redirect(self):
        """
        Test if the homepage redirects correctly for anonymous users.
        """
        self.user_logout()  # Ensure no user is logged in
        response = self.client.get('/')  # Access the homepage
        self.assertEqual(
            response.status_code,
            302,
            "Homepage did not redirect successfully for anonymous users."
        )
        # Check if the redirection URL is correct
        self.assertEqual(
            response['Location'],
            '/software/features',  # Adjust this if the redirection target changes
            "Homepage did not redirect to the expected URL."
        )
