#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    myList = my_list.copy()
    myList.reverse()
    for i in myList:
        print("{:d}".format(i))
