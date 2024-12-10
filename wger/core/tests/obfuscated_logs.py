"""

Author : Nikolaos Kales r0927517
Category : Privacy Compliance
Test 3.1: Obfuscated Logs
Purpose: nsure logs do not contain sensitive identifiers

"""

import os
from django.test import TestCase

class PrivacyComplianceTest(TestCase):
    def test_obfuscated_logs(self):
        # Path to your log file
        log_path = os.path.join(os.path.dirname(__file__), '../../../application.log')

        # Check if the log file exists
        self.assertTrue(os.path.exists(log_path), f"Log file not found at {log_path}")

        # Open the log file and search for sensitive data patterns
        with open(log_path, 'r') as log_file:
            log_content = log_file.read()

        # Patterns to check for sensitive data
        sensitive_patterns = ["password", "token", "secret", "credit card"]
        
        # Ignore schema creation logs or harmless entries
        harmless_contexts = ["CREATE TABLE", "params None"]

        for pattern in sensitive_patterns:
            # Check if sensitive pattern is found outside harmless contexts
            if any(pattern in line and not any(context in line for context in harmless_contexts)
                   for line in log_content.splitlines()):
                self.fail(f"Sensitive data ('{pattern}') found in logs!")