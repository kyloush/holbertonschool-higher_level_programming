#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for element in set_1:
        if element not in set_2:
            diff.add(element)
    for element in set_2:
        if element not in set_1:
            diff.add(element)
    return sorted(diff)
