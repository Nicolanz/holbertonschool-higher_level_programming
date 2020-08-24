#!/usr/bin/python3
"""Post an email to a website"""
from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    site = argv[1]
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email)
    email = data.encode('ascii')

    res = urllib.request.Request(site, email)

    with urllib.request.urlopen(res) as obj:
        body = obj.read()
        print(body.decode('utf-8'))
