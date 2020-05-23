#!/usr/bin/python3
"""Function to print a text.
If it finds a specific letter
it will print two newlines.
This fucntion provides a .txt file
to test"""


def text_indentation(text):
    """Text

    Arguments:
        text {[str]} -- [text]
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if (text[i] == "." or text[i] == "?" or text[i] == ":"):
            print("\n")
    print()
