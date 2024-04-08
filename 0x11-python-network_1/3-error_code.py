#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL, and displays
 the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL and read the response
        with urllib.request.urlopen(url) as response:
            # Decode the body of the response
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code:", e.code)
