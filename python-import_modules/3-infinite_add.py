#!/usr/bin/python3
import sys

if _name_ == "_main_":
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)

print(total)