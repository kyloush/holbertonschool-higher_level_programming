#!/usr/bin/python3
def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0

    for i in range(len(s) - 1):
        current_value = roman_map[s[i]]
        next_value = roman_map[s[i+1]]

        if current_value < next_value:
            total -= current_value
        else:
            total += current_value

    total += roman_map[s[-1]]

    return total
