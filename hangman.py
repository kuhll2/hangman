# Program that simulates a game of hangman

import random
import re


def read_file():
    with open("words_alpha.txt", "r") as file:  # Read in dictionary of words
        dictionary = [line.strip() for line in file]
    return dictionary


# pick_word fcn
def pick_word(dictionary):
    """This function uses a dictionary text file to pick the word to guess"""
    word = ""
    while len(word) < 4: # we want a word that is 4 letters or longer
        word = random.choice(dictionary)
    return word.lower()

# Prints board and guessed letters
def print_board():
    print(output)
    print("The letters guessed so far are: ", guessed_letters)
    print(" ")

# Picks a word from the dictionary for user to guess
def get_word(dictionary):
    word = pick_word(dictionary)
    letters = list(word)
    output = []
    for i in range(len(word)):
        output.append('_')
    return word, letters, output

def get_indexes(count, letters, guess):
    indexes = []
    for x in range(count):
        if len(indexes) == 0:
            indexes.append(letters.index(guess))
        else:
            indexes.append(letters.index(guess, letters.index(guess) + x))
    return indexes


if __name__ == "__main__":
    guessed_letters = [] # Declare vars
    wrong_left = 10
    word, letters, output = get_word(read_file())
    print("The word to guess is", len(word), "letters long. If you guess 10 incorrect letters, you lose.")
    print(output) # Print word details

    # Run game loop
    while wrong_left != 0:
        guess = input("Please guess a letter or type 'quit' to exit game: ").lower()
        if guess == 'quit':
            print("Better luck next time!")
            break
        if guessed_letters.count(guess) > 0:
            print("You already guessed that letter!")
            continue
        count = letters.count(guess)
        if count == 0 and guess != " ":
            wrong_left -= 1
        indexes = get_indexes(count, letters, guess)
        print("There is", count, guess, "- You have", wrong_left, "guesses before you lose.")
        if output.count('_') == 0:
            print("Congrats!! You found the word!", output)
            correct = True
            break
        for n in range(len(indexes)):
            output[indexes[n - 1]] = letters[indexes[n - 1]]
        guessed_letters.append(guess)
        print_board()
    print("The word was", word)