#!/usr/bin/python3
"""7 error with requets"""
import requests
from sys import argv

if __name__ == "__main__":

    try:
        obj = requests.get(argv[1])
        if obj.status_code >= 400:
            print("Error code: {:d}".format(obj.status_code))
        else:
            print(obj.text)
    except:
        pass

    # obj = requests.get(argv[1])
    # if obj.status_code >= 400:
    #     print("Error code {}".format(obj.status_code))
    # else:
    #     print(obj.text)
