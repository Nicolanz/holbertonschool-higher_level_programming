#!/usr/bin/python3
def text_indentation(text):
    i =0
    c = i-1
    for i in range(len(text)):
        if text[c] == " ":
            print(text[i],end="")
        if (text[i] == "." or text[i] == "?" or text[i] ==":"):
            print("\n")
        c = c+1
    print()