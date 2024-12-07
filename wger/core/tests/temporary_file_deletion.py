"""

Author : Nikolaos Kales r0927517
Category : Data Retention
Test 2.1 : Temporary File Deletion
Purpose: Validate that temporary files (e.g., logs or cache) are deleted after use

"""

import os

def test_temporary_file_deletion():
    temp_dir = "path/to/temp"  # Replace with actual path
    assert not os.listdir(temp_dir), "Temporary files not deleted!"

test_temporary_file_deletion()
