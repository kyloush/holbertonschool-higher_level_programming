from game import HangmanGame

game = HangmanGame(max_error=10)
olders = set()

while True:
    guessed_letters = input('enter a letter (exit to quit): ')
    if guessed_letters == 'exit':
        break
    if not len(guessed_letters) == 1:
        print('must be a single character')
        continue
    elif not guessed_letters.isalpha():
        print('must be a letter')
        continue
    elif guessed_letters in olders:
        print('already tried')
    else: 
        olders.add(guessed_letters)
        game.guess(guessed_letters)

    if game.is_won():
        print(f"You won! The word was: {game.word}")
        print('write "i love that game" to restart')
        restart = input('')
        if restart == 'i love that game':
            continue
        else:
            break
    elif game.is_lost():
        print(f"You lost! The word was: {game.word}")
        print('write "i love that game" to restart')
        restart = input('')
        if restart == 'i love that game':
            continue
        else:
            break