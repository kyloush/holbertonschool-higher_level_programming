#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # or raise an error if empty list is invalid

    highest = my_list[0]
    for num in my_list:
        if num > highest:
            highest = num
    return highest
