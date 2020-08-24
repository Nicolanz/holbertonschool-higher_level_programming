#!/usr/bin/python3
"""POST with requests"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    req = requests.post(url, data=email)
    print(req.text)
