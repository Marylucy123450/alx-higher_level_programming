#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argumentand displays the body of the response
curl -s -X DELETE "$1"
