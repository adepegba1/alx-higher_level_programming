#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
