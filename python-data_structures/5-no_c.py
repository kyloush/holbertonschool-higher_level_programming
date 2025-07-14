#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if ord(char) != 99 and ord(char) != 67:  # 99 = 'c', 67 = 'C'
            result += char
    return result
