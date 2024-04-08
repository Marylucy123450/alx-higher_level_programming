#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Fetching the URL and reading the response
with urllib.request.urlopen(url) as response:
    # Getting the body of the response
    body = response.read()

    # Printing the body of the response in the specified format
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
