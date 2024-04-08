#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Send a POST request to the server
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        # Parse the response as JSON
        json_response = response.json()

        # Check if the JSON is empty
        if json_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_response['id'], json_response['name']))

    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
