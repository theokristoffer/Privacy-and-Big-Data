"""

Author : Nikolaos Kales r0927517
Category : Privacy Compliance
Test 3.2 : Exclusion from Backups
Purpose: Verify sensitive data is excluded from backups

"""

import os

def test_backup_exclusion():
    backup_dir = "path/to/backup"  # Replace with actual path
    sensitive_file = "path/to/credentials.json"
    backups = os.listdir(backup_dir)
    for backup in backups:
        assert sensitive_file not in backup, "Sensitive data found in backups!"

test_backup_exclusion()
