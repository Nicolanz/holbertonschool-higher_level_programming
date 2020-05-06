#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newList = my_list
    if(idx < 0 or idx >= len(newList)):
        return (newList)
    for i in newList:
        if (i - 1 == idx):
            newList.remove(i)
    return(newList)
