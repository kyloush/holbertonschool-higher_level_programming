import random
from config import SHIP_SPECS

class Ship:
    def __init__(self, length, name=None):
        self.length = length
        self.positions = []
        self.hits = set()
        self.name = name

    def occupied_positions(self, positions):
        self.positions = positions

    def hit_tracking(self, coord):
        if coord in self.positions:
            self.hits.add(coord)

    def sunken(self):
        return set(self.positions) == self.hits

def prepare_fleet():
    names = ['Jetski', 'Sail Boat', 'Yellow Submarine', 'Yacht']
    return [Ship(SHIP_SPECS[i], names[i]) for i in range(len(SHIP_SPECS))]

def random_ship_positioning(board, ship):
    height = len(board)
    width = len(board[0])
    placed = False

    while not placed:
        orientation = random.choice(["H", "V"])
        if orientation == "H":
            row = random.randint(0, height - 1)
            col = random.randint(0, width - ship.length)
            positions = [(row, col + i) for i in range(ship.length)]
        else:
            row = random.randint(0, height - ship.length)
            col = random.randint(0, width - 1)
            positions = [(row + i, col) for i in range(ship.length)]

        if all(board[r][c] == '_' for r, c in positions):
            for r, c in positions:
                board[r][c] = 'S'
            ship.positions = positions
            placed = True

def deploy_fleet(board, fleet):
    lookup = {}
    for ship in fleet:
        random_ship_positioning(board, ship)
        for pos in ship.positions:
            lookup[pos] = ship
    return lookup

def shot_processing(coord, board, lookup):
    if coord in lookup:
        ship = lookup[coord]
        ship.hit_tracking(coord)
        board[coord[0]][coord[1]] = '#'
        if ship.sunken():
            print(f"{ship.name} is out of service!")
            return "sunk"
        print("hit!")
        return "hit"
    else:
        board[coord[0]][coord[1]] = '~'
        print("miss!")
        return "miss"