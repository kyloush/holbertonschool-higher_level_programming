#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for num in my_list:
        if num % 2 == 0:
            print(f"{num} is divisible by 2")
        else:
            print(f"{num} is not divisible by 2")
