#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldo = abs(number) % 10
if number < 0:
    ldo = -ldo
if ldo > 5:
    print(f"Last digit of {number} is {ldo} and is greater than 5")
elif ldo == 0:
    print(f'Last digit of {number} is {ldo} and is 0')
else:
    print(f"Last digit of {number} is {ldo} and is less than 6 and not 0")
