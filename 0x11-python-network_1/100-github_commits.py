#!/usr/bin/python3
"""Print last 10 commits with the github API"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    try:
        obj = requests.get(url)
        commitsDict = obj.json()
        for i in range(0, 10):
            print("{}: {}".format(
                commitsDict[i]['sha'],
                commitsDict[i]['commit']['author']['name'])
            )
    except:
        pass
