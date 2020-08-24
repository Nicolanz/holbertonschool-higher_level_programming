#!/usr/bin/python3
"""request using requests"""
import requests

if __name__ == "__main__":
    obj = requests.get('https://intranet.hbtn.io/status')
    print(
        "Body response:\n\t- type: {}\n\t- content: {}"
        .format(type(obj.text), obj.text)
        )
