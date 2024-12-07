"""

Author : Nikolaos Kales r0927517
Category : Network Traffic
Test 4.1 : HTTPS Enforcement
Purpose: Check that all network communication uses HTTPS

"""

import requests

def test_https_enforcement():
    url = "http://example.com/api"  # Replace with actual URL
    response = requests.get(url)
    assert response.url.startswith("https://"), "Non-secure HTTP connection detected!"

test_https_enforcement()
