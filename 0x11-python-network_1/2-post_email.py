#!/usr/bin/python3
"""
takes the URL  and an email sends a POST request to passed URL displays body
"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
