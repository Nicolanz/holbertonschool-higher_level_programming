#!/usr/bin/python3
"""Module to list states which have a N as initia
vpepalue"""
from sys import argv, exit
import MySQLdb

if (len(argv) < 4):
    pass
else:
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    except:
        exit(1)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    result = cursor.fetchall()
    for i in result:
        if i[1][0] == "N":
            print(i)
    db.close()
