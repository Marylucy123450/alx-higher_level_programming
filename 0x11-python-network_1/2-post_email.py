#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to
 the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')  # Encode the data to bytes

    # Send a POST request to the URL with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        print(body)
