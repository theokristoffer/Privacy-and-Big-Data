"""

Author : Nikolaos Kales r0927517
Category : Data Storage 
Test 1.1 : Plain Text Credential Check
Purpose : Ensure sensitive data (e.g., user passwords) are not stored in plain text
Pre-mitigation Behavior : Test should identify passwords stored in plain text
Post-mitigation Behavior : Test should fail to access passwords due to encryption

"""

# 

import os
import json

def test_plaintext_credentials():
    credentials_file = "path/to/credentials.json"  # Replace with actual path
    assert os.path.exists(credentials_file), "Credentials file does not exist."
    
    with open(credentials_file, "r") as file:
        data = json.load(file)
        assert "password" not in data, "Plain text password found!"

test_plaintext_credentials()
