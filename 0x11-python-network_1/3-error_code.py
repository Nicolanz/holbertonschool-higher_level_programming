#!/usr/bin/python3
"""print status error if exists"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as obj:
            body = obj.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
