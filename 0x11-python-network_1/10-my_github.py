#!/usr/bin/python3
"""Get with requests to github"""
import requests
from sys import argv, exit

if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = argv[1]
    passw = argv[2]

    obj = requests.get(url, auth=(user, passw))

    try:
        var = obj.json()
        print(var['id'])
    except:
        pass
