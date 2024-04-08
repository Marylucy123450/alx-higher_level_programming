#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL, and displays
the body of the response. If the HTTP status code is greater than or equal to
400, it prints "Error code:" followed by the value of the HTTP status code"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request to the URL
    response = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)  # Display the body of the response
