#!/usr/bin/python3
"""
takes the URL and email address and sends POST requests  to passed URL with
email parameter and displays body of response
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
