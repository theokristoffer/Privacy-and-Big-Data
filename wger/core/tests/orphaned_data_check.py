"""

Author : Nikolaos Kales r0927517
Category : Data Retention
Test 2.2 : Orphaned Data Check
Purpose: Identify orphaned data (e.g., old user data)

"""

import sqlite3

def test_orphaned_data():
    conn = sqlite3.connect("path/to/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE last_login IS NULL")
    rows = cursor.fetchall()
    assert not rows, "Orphaned data found!"

test_orphaned_data()
