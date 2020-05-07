#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set()
    for i in set_1:
        for j in set_2:
            if (i == j):
                break
            else:
                continue
        if(i != j):
            new.add(i)
    i = 0
    j = 0
    for i in set_2:
        for j in set_1:
            if (i == j):
                break
            else:
                continue
        if(i != j):
            new.add(i)
    return(new)
