#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if ord(char) != 99 and ord(char) != 67:
            result += char
    return result
