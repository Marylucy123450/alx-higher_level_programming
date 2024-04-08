#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL, and displays
the value of the variable X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the value of the X-Request-Id header if it exists
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
