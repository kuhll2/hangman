# Program that simulates a game of hangman

import random
import re


# pick_word fcn
def pick_word(dictionary, length):
    """This function uses a dictionary text file to pick the word to guess"""
    while length < 4: # we want a word that is 4 letters or longer
        word = random.choice(dictionary)
        length = len(word)
    return word.lower(), length

# Declare vars
guessed_letters = []
wrong_left = 10
correct = False

# Read in dictionary of words
file = open("words_alpha.txt", "r")
dictionary = [line.strip() for line in file]

# Get word and length
length = 0
word, length = pick_word(dictionary, length)
letters = list(word)
output = []
for i in range(length):
    output.append('_')

# Print word details
print("The word to guess is", length, "letters long. If you guess 10 incorrect letters, you lose.")
print(output)

while wrong_left != 0 and not correct:
    count = 0
    indexes = []
    guess = input("Please guess a letter or type 'quit' to exit game: ").lower()
    if guess == 'quit':
        print("Better luck next time!")
        break
    count = letters.count(guess)
    if count == 0:
        wrong_left -= 1
    for x in range(count):
        if len(indexes) == 0:
            indexes.append(letters.index(guess))
        else:
            indexes.append(letters.index(guess, indexes[x]))
    print("There is", count, guess, "- You have", wrong_left, "guesses before you lose.")
    if output.count('_') == 0:
        print("Congrats!! You found the word!", output)
        correct = True
    for n in range(len(indexes)):
        print(indexes)
        output[indexes[n - 1]] = letters[indexes[n - 1]]
    guessed_letters.append(guess)
    print(output)
    print("The letters guessed so far are: ", guessed_letters)
    print(" ")
print("The word was", word)