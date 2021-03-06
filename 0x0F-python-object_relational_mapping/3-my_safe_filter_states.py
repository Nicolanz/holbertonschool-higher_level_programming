#!/usr/bin/python3
"""Module to list matches with the state given
as arg"""
from sys import argv, exit
import MySQLdb

if (len(argv) < 5):
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
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM states  WHERE name = %(searched)s\
        ORDER BY id ASC", {'searched': argv[4]})
        result = cursor.fetchall()
    for i in result:
        print(i)
