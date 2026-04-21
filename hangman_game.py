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
        self.__correct_letters = set()
        self.__wrong_letters = set()
        self.__wrong_guesses = 0
        self.__max_attempts = 9  # Changed to 9

    # Randomly select a word from the word bank
    def __choose_word(self):
        return random.choice(self.hangman_word_bank)
    
    # Shows the selected word with underscores for missing letters
    def __display_word(self):
        display = ""
        for letter in self.__word:
            if letter in self.__correct_letters:
                display += letter + " "
            else:
                display += "_ "

        return display.strip()
    
    # Resets the game state for a new round
    def __reset_game(self):
        self.__word = self.__choose_word()
        self.__correct_letters = set()
        self.__wrong_letters = set()
        self.__wrong_guesses = 0

    # This is the start of the game here.
    def start_game(self):
        print("Welcome to Hangman!")
        print("(Hint: It's boardgame themed!)")

        # Starts a game loop
        while True:  # Game loop (for replay)
            self.__reset_game()

            # Until the max attempts are made, the user can continue to guess letters.
            while self.__wrong_guesses < self.__max_attempts:
                print("\nWord:", self.__display_word())
                print("Correct letters:", sorted(self.__correct_letters))
                print("Wrong letters:", sorted(self.__wrong_letters))
                print("Attempts left:", self.__max_attempts - self.__wrong_guesses)

                guess = input("Guess a letter: ").lower()

                # Makes sure that a letter is being inputted.
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single letter.")
                    continue

                # Makes sure the letter hasn't been asked.
                if guess in self.__correct_letters or guess in self.__wrong_letters:
                    print("You already guessed that letter.")
                    continue

                # Checks if the guess is correct
                if guess in self.__word:
                    print("Correct guess!")
                    self.__correct_letters.add(guess)
                else:
                    print("Wrong guess!")
                    self.__wrong_letters.add(guess)
                    self.__wrong_guesses += 1

                # Checks win condition
                if all(letter in self.__correct_letters for letter in self.__word):
                    print("\nWord:", self.__word)
                    print("Congratulations! You guessed the word!")
                    break

            # Without any attempts left, the user lost the game
            if self.__wrong_guesses >= self.__max_attempts:
                print("\nGame Over! You ran out of attempts.")
                print("The word was:", self.__word)

            # Asks to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()

            if play_again != "y":
                print("Thanks for playing!")
                break

# Runs the game 
if __name__ == "__main__": 
    game = HangmanGame() 
    game.start_game()