#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Create the authentication string using Basic Authentication
    auth = (username, password)

    # Make a GET request to the GitHub API to fetch user information
    response = requests.get('https://api.github.com/user', auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        user_info = response.json()

        # Display the user's id
        print(user_info['id'])
    else:
        print("None")
