"""

Author : Nikolaos Kales r0927517
Category : Privacy Compliance
Test 3.2 : Exclusion from Backups
Purpose: Verify sensitive data is excluded from backups

"""

import os
from django.test import TestCase

class PrivacyComplianceTest(TestCase):
    def test_exclusion_from_backups(self):
        # Path to backup directory (replace with actual path)
        backup_path = "/Users/nikolaos/KU_Leuven/GitHub/wger/backups"

        # Check if the backup directory exists
        self.assertTrue(os.path.exists(backup_path), f"Backup directory not found at {backup_path}")

        # Search for sensitive files that shouldn't be in backups
        sensitive_files = ["application.log", "db.sqlite3", "secret.key"]
        for root, dirs, files in os.walk(backup_path):
            for sensitive_file in sensitive_files:
                self.assertNotIn(
                    sensitive_file, files,
                    f"Sensitive file '{sensitive_file}' found in backup!"
                )
