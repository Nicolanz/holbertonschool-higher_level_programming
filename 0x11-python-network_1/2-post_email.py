#!/usr/bin/python3
"""Post an email to a website"""
from sys import argv
import urllib.parse
import urllib.request

site = argv[1]
mail = {'email': argv[2]}


data = urllib.parse.urlencode(mail)
email = data.encode('utf-8')

with urllib.request.urlopen(site, email) as obj:
    body = obj.read()

print(body.decode('utf-8'))
