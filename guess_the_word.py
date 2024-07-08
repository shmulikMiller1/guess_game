import random

with open('my_words.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

players_dict = {}
guessed_words = []
guessed_letters = ""
num_players = int(input("please enter the number of players: "))
for i in range(num_players):
    name = input("please enter your name: ")
    players_dict[name] = 0
num_words = int(input("please enter the number of words to guess: "))
for i in range(num_words):
    guess_word = random.choice(words)
    if guess_word in guessed_words:
        guess_word = random.choice(words)
    else:
        guessed_words.append(guess_word)
    hidden_word = "_" * len(guess_word)
    hidden_word = list(hidden_word)
    print(hidden_word)
    while "_" in hidden_word:
        for key in players_dict:
            letter_guess = input(f"{key} enter your letter guess: ")
            while len(letter_guess) > 1 or letter_guess in hidden_word:
                letter_guess = input(f"{key} enter your letter guess: ")
            guessed_letters += letter_guess
            for j in range(len(guess_word)):
                if guess_word[j] == letter_guess:
                    hidden_word[j] = letter_guess
                    players_dict[key] += 1
            print(hidden_word)
            if "_" not in hidden_word:
                break
    print(guess_word)
    guessed_letters = ""
max_points = 0
winner = max(players_dict, key= players_dict.get)
points = players_dict[winner]
print(players_dict)
print(guessed_words)
print(f"the winner in this play is {winner} with {points} points")













