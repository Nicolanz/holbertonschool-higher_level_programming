#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if(argv[2] != '+' and argv[2] != '-' and
       argv[2] != '*' and argv[2] != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if(argv[2] == '+'):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        if(argv[2] == '-'):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        if(argv[2] == '/'):
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        if(argv[2] == '*'):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
