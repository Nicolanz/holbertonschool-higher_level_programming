#!/usr/bin/python3
"""Print body of a request"""
from urllib import request


with request.urlopen("https://intranet.hbtn.io/status") as obj:
    req = obj.read()

print("Body response:\n\
    \t- type: {}\n\
    \t- content: {}\n\
    \t- utf8 content: {}".format(type(req), req, req.decode("UTF-8")))
