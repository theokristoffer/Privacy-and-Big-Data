"""

Author : Nikolaos Kales r0927517
Category : Privacy Compliance
Test 3.1: Obfuscated Logs
Purpose: nsure logs do not contain sensitive identifiers

"""

def test_log_anonymization():
    log_file = "path/to/logs/app.log"  # Replace with actual log file
    with open(log_file, "r") as file:
        logs = file.read()
        assert "user_email" not in logs, "Sensitive email found in logs!"

test_log_anonymization()
