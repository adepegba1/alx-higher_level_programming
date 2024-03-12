#!/usr/bin/python3
""" sends request to URL and displays the value of the X-request-ID
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
