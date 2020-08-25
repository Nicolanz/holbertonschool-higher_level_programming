#!/usr/bin/python3
"""POST json response content"""
import requests
from sys import argv, exit

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = {'q': argv[1]}
    except:
        q = ""
    req = requests.post(url, data=q)

    try:
        var = req.json()
    except:
        print("Not a valid JSON")
        exit(1)

    if (len(var) <= 0):
        print("No result")
    else:
        print("[{}] {}".format(var['id'], var['name']))
