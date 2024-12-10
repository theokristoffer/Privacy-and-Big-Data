"""

Author : Nikolaos Kales r0927517
Category : Data Retention
Test 2.1 : Temporary File Deletion
Purpose: Validate that temporary files (e.g., logs or cache) are deleted after use

"""

import os
import tempfile
from django.test import TestCase

class TemporaryFileDeletionTest(TestCase):
    def test_temporary_file_deletion(self):
        temp_dir = tempfile.gettempdir()
        print(f"Checking temporary directory: {temp_dir}")

        # Filter for application-specific temporary files
        app_temp_files = [
            f for f in os.listdir(temp_dir)
            if f.startswith("your_app_prefix_")  # Replace with a prefix if your app creates temp files
        ]

        self.assertFalse(
            app_temp_files,
            f"Temporary files not deleted! Found: {app_temp_files}"
        )


