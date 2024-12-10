"""

Author : Nikolaos Kales r0927517
Category : Data Retention
Test 2.2 : Orphaned Data Check
Purpose: Identify orphaned data (e.g., old user data)

"""

import sqlite3
from django.test import TestCase

class OrphanedDataTest(TestCase):
    def test_orphaned_data(self):
        # Path to your SQLite database
        db_path = "/Users/nikolaos/KU_Leuven/GitHub/wger/db.sqlite3"

        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query for orphaned user data (e.g., users without a last login)
        cursor.execute("SELECT * FROM auth_user WHERE last_login IS NULL")
        rows = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Assert no orphaned data
        self.assertFalse(rows, f"Orphaned data found! Rows: {rows}")


