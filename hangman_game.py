# Katherine Smith
# CIS256 Spring 2026
# Exercise Assignment 4

# Temp Comment to self of this location: 
# C:\Users\catbl\OneDrive\Desktop\HW\CIS256 - Python II\CIS256_Katherine_Smith_EX4

# Imports random so we can randomly chose from the bank.
import random

class HangmanGame:
    # Word bank with board game themed words
    hangman_word_bank = [
        "catan",
        "monopoly",
        "chess",
        "risk",
        "clue",
        "scrabble",
        "jenga",
        "checkers",
        "cranium"
    ]

    def __init__(self):
        # Private attribute for the selected word
        self.__word = self.__choose_word()

    # Randomly select a word from the word bank
    def __choose_word(self):
        return random.choice(self.hangman_word_bank)

    # For testing reasons, I need to make sure a word is being chosen.
    def start_game(self):
        print("Selected word:", self.__word)


# Runs the game
if __name__ == "__main__":
    game = HangmanGame()
    game.start_game()