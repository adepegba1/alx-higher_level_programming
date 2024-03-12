#!/usr/bin/python3
"""
takes URL sends request to the URL and displays the value of
X-Request-Id
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-ID'))
