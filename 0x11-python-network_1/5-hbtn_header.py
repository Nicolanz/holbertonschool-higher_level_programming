#!/usr/bin/python3
"""Header variable with request"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        obj = requests.get(argv[1])
        print(obj.headers['X-Request-Id'])
    except:
        pass
