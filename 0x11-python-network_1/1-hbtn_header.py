#!/usr/bin/python3
import urllib.request
from sys import argv
"""Displays the X-Request-Id variable found un a header"""
try:
    with urllib.request.urlopen(argv[1]) as response:
        html = response.headers['X-Request-Id']
        print(html)
except:
    pass
