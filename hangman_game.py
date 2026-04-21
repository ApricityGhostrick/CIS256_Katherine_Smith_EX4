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
        self.__guessed_letters = set()
        self.__wrong_guesses = 0
        self.__max_attempts = 100  # Temporary for testing win condition, later will be 9

    # Randomly select a word from the word bank
    def __choose_word(self):
        return random.choice(self.hangman_word_bank)
    
    # This is the start of the game here.
    def start_game(self):
        print("Welcome to Hangman!")

        # Until the max attempts are made, the user can continue to guess letters.
        while self.__wrong_guesses < self.__max_attempts:
            guess = input("Guess a letter: ").lower()

            # Makes sure that a letter is being inputted.
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            # Makes sure the letter hasn't been asked.
            if guess in self.__guessed_letters:
                print("You already guessed that letter.")
                continue

            # Add guess to the set
            self.__guessed_letters.add(guess)

            # Checks if the guess is correct
            if guess in self.__word:
                print("Correct guess!")
            else:
                print("Wrong guess!")
                self.__wrong_guesses += 1

            # TEMP: Shows progress
            print("Guessed letters:", self.__guessed_letters)

            # TEMP: Reveals word for testing
            print("Word (for now):", self.__word)

            # Checks for win condition
            if all(letter in self.__guessed_letters for letter in self.__word):
                print("You guessed the word!")
                break

        print("Game ended.")
        
        
# Runs the game
if __name__ == "__main__":
    game = HangmanGame()
    game.start_game()