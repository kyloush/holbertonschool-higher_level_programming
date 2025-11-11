def get_board_size():
    while True:
        start = input('"start" to start / "stop" to stop: ')
        if start.lower() == 'stop':
            print('why did you run the code')
            break
        if start.lower() == 'start':
            print('good luck, I wish you lose')

            try:
                width = int(input('Board width: '))
                if width < 4 or width > 10:
                    print('Width must be between 4 and 10. Are you dumb')
                    continue

                height = int(input('Board height: '))
                if height < 4 or height > 10:
                    print('Height must be between 4 and 10. Are you dumb')
                    continue

                return width, height

            except ValueError:
                print('Dumbass, enter valid integers for width and height.')

SHIP_SPECS = [1, 2, 3, 4]