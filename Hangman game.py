logo="""

 _____                              _____
|  |  |___ ___ ___ _____ ___ ___   |   __|___ _____ ___
|     | .'|   | . |     | .'|   |  |  |  | .'|     | -_|
|__|__|__,|_|_|_  |_|_|_|__,|_|_|  |_____|__,|_|_|_|___|
              |___|

"""
import random

word_list = ['game', 'python', 'hangman', 'practice', 'project']
random_word = random.choice(word_list)
print(random_word)
print("***********************************")
print("welcome to Hangman Game")
print("guess the letters in limited attempts or lose")
print("***********************************")

display = ["_"] * len(random_word)
print(*display, "\n")
lives = 6

while lives > 0 and "_" in display:
    letter = input("Guess a letter: ")
    found = False  # Flag to check if the guessed letter is found
    for position in range(len(random_word)):
        if letter == random_word[position]:
            display[position] = random_word[position]
            found = True  # Letter found in the word
    if not found:
        lives -= 1
        print(f"remaining lives = {lives}")
        print("try again!!!")
    print("your guess is = ", *display, "\n")
    if "_" not in display:
        print("you won the game")
        break

if lives == 0:
    print("you lose")
    print(f"the correct answer is {random_word}")














