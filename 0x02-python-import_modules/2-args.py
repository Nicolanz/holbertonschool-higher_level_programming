#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv) - 1
    if (size < 1):
        print("0 arguments.")
    elif (size == 1):
        print("1 argument:".format(size))
    else:
        print("{:d} arguments:".format(size))
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
