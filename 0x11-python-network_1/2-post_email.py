#!/usr/bin/python3
"""Post an email to a website"""
from sys import argv
import urllib.parse
import urllib.request

site = argv[1]
email = {'email': argv[2]}


data = urllib.parse.urlencode(email)
mail = data.encode('utf-8')

req = urllib.request.Request(site, mail)

with urllib.request.urlopen(req) as obj:
    body = obj.read()
    print(body.decode('utf-8'))
