#!/usr/bin/python3
"""Displays the X-Request-Id variable found un a header"""
import urllib.request
from sys import argv

try:
    with urllib.request.urlopen(argv[1]) as response:
        html = response.headers['X-Request-Id']
        print(html)
except:
    pass
