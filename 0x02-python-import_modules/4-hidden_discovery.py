#!/usr/bin/python3.4
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    b = 0
    for i in names:
        if (i[b] != '_'):
            print(i)
