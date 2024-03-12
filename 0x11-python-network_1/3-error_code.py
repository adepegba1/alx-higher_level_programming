#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response in utf-8
"""
from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(res.read().decode('utf-8'))
    except urllib.error.URLError as e:
            print("Error code: {}".format(e.code))
