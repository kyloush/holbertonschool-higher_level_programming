#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit_of = int(str(number)[-1])
if number < 0: 
    Last_digit_of = -Last_digit_of
if Last_digit_of > 5:
    print(f"the last digit of {number} is {Last_digit_of} and is greater than 5")
elif Last_digit_of == 0:
    print(f'the last digit of {number} is {Last_digit_of} and is 0')
else:
    print(f"the last digit of {number} is {Last_digit_of} and is less than 6 and not 0")
