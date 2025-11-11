def get_random_word():
    import random
    with open("wordlist.txt") as list:
        text = list.read().strip()
    word = text.split()
    random_word = random.choice(word)
    return random_word