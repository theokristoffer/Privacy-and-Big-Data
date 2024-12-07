"""

Author : Nikolaos Kales r0927517
Category : Data Storage 
Test 1.2 : Database Encryption Check
Purpose: Ensure sensitive fields (e.g., tokens) in the database are encrypted.
Implementation: Query database directly and verify encryption format.

"""

import sqlite3

def test_encrypted_fields():
    conn = sqlite3.connect("path/to/database.db")  # Replace with actual path
    cursor = conn.cursor()
    cursor.execute("SELECT token FROM users")
    tokens = cursor.fetchall()
    for token in tokens:
        assert not token[0].isalnum(), "Unencrypted token found!"

test_encrypted_fields()
