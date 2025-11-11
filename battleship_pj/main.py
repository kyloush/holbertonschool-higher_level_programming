from config import get_board_size
from board import create_empty_grid, print_board, valid_shot_coord, cpu_shooting
from ships import prepare_fleet, deploy_fleet, shot_processing

def main():
    width, height = get_board_size()
    player_board = create_empty_grid(width, height)
    cpu_board = create_empty_grid(width, height)

    player_fleet = prepare_fleet()
    cpu_fleet = prepare_fleet()

    player_lookup = deploy_fleet(player_board, player_fleet)
    cpu_lookup = deploy_fleet(cpu_board, cpu_fleet)

    player_remaining = len(set(player_lookup.values()))
    cpu_remaining = len(set(cpu_lookup.values()))

    while player_remaining > 0 and cpu_remaining > 0:
        print("your board:")
        print_board(player_board)
        print("computer's board:")
        print_board(cpu_board, hide_ships=True)

        shot = valid_shot_coord(width, height)
        result = shot_processing(shot, cpu_board, cpu_lookup)
        if result == "sunk":
            cpu_remaining -= 1
        if cpu_remaining == 0:
            print("you won... why are you smart")
            break

        cpu_shot = cpu_shooting(width, height)
        print(f"computer fired at {chr(65 + cpu_shot[0])}{cpu_shot[1] + 1}")
        result = shot_processing(cpu_shot, player_board, player_lookup)
        if result == "sunk":
            player_remaining -= 1
        if player_remaining == 0:
            print("you lose! HA deep piece of ship")
            break

        print("game is over.")

if __name__ == '__main__':
    main()
