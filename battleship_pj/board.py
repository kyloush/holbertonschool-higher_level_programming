import random


previous_shots = set()
cpu_shots_taken = set()

def create_empty_grid(width, height):
    return [['_' for _ in range(width)] for _ in range(height)]

def print_headers(width):
    print("  ", end="")
    for col in range(1, width + 1):
        print(col, end=" ")
    print()

def print_board(grid, hide_ships=False):
    width = len(grid[0])
    print_headers(width)
    for i, row in enumerate(grid):
        row_label = chr(65 + i)
        row_str = row_label + ' '
        for cell in row:
            if hide_ships and cell == 'S':
                row_str += '_ '
            else:
                row_str += cell + ' '
        print(row_str)

def valid_shot_coord(width, height):
    while True:
        user_input = input("Enter shot coordinates: ").strip().upper()
        if len(user_input) < 2:
            print("rewrite.")
            continue

        row_label = user_input[0]
        col_header = user_input[1:]

        if not row_label.isalpha() or not col_header.isdigit():
            print("Use letter+number.")
            continue

        row = ord(row_label) - ord('A')
        col = int(col_header) - 1

        if not (0 <= row < height and 0 <= col < width):
            print("you are out of the grid")
            continue

        if (row, col) in previous_shots:
            print("do you know how to read a grid")
            continue

        return (row, col)

def cpu_shooting(width, height):
    while True:
        shot = (random.randint(0, height - 1), random.randint(0, width - 1))
        if shot not in cpu_shots_taken:
            cpu_shots_taken.add(shot)
            return shot