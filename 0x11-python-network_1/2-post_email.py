#!/usr/bin/python3
"""Post an email to a website"""
from sys import argv
import urllib.parse
import urllib.request

site = argv[1]
mail = {'email': argv[2]}


data = urllib.parse.urlencode(mail)
data = data.encode('ascii')

with urllib.request.urlopen(site, data) as obj:
    body = obj.read()

print(body.decode('utf-8'))
