#!/usr/bin/python3
"""Module to list a database"""
from sys import argv, exit
import MySQLdb

if (len(argv) < 4):
    pass
else:
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
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
        print(i)
    db.close()
