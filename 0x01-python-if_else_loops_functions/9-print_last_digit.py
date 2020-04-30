#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        lastnumber = number % 10
    else:
        tmp = number * -1
        lastnumber = tmp % 10
    print("{:d}".format(lastnumber), end="")
    return lastnumber
