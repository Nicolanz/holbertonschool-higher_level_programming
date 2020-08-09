#!/usr/bin/python3
"""Consults cities of a given state"""
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
        cursor.execute("SELECT cities.name FROM cities WHERE cities.state_id\
            IN (SELECT id from states WHERE states.name\
                    = %(searched)s)", {'searched': argv[4]})
        result = cursor.fetchall()
    if (len(result) > 0):
        for i in range(len(result)):
            if (i+1 == len(result)):
                print("{:s}".format(result[i][0]))
            else:
                print("{:s}, ".format(result[i][0]), end='')
    else:
        print()
