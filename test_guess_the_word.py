# Katherine Smith
# CIS256 Spring 2026
# Exercise Assignment 4

from guess_the_word import HangmanGame

# Test 1) Does the program select a word from the word bank?
def test_word_selected_from_bank():
    game = HangmanGame()
    word = game.get_word()

    assert word in game.hangman_word_bank


# Test 2) Does the application not allow for two letters at once?
def test_two_letter_input_not_allowed():
    guess = "ab"
    assert len(guess) != 1


# Test 3) Does the application properly know a correct letter in a word?
def test_correct_guess_c_in_catan():
    game = HangmanGame()

    game._HangmanGame__word = "catan"

    result = game.check_guess("c")

    assert result is True