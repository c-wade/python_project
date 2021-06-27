"""
File: hangman.py
Author: Wade Chao
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    hangman()


def hangman():
    """
    Hangman game:
    1. Get the random answer and initialize guess
    2. Get a guess character and check if it is in the answer
    3. Get result if win or lose condition is fulfilled
    """
    answer = random_word()
    guess = init_guess(answer)
    turns = N_TURNS
    end_game = False
    while not end_game:
        guess_char = get_guess_char(guess, turns)
        guess, turns = match_guess_char(guess, answer, guess_char, turns)
        end_game = get_result(guess, answer, turns)


def init_guess(ans):
    """
    Initialize guess as long as answer with '-' symbol
    """
    result = ''
    for i in ans:
        result += '-'
    return result


def get_guess_char(guess, turns):
    """
    Get user guess character
    """
    while True:
        print('=============================')
        print(f'The word looks like: {guess}')
        print(f'You have {turns} guesses left')
        guess_char = str(input('Your guess:')).upper()
        if guess_char.encode().isalpha() and len(guess_char) == 1:
            return guess_char
        else:
            print('!! Invalid format !!')


def match_guess_char(guess, answer, guess_char, turns):
    """
    Check if the guess is in the answer,
     - if correct, add the correct character in guess and return
     - if not correct, return the original guess & turns minus one
    """
    result, correct = '', False
    for i in range(len(answer)):
        if guess_char == answer[i]:
            result += answer[i]
            correct = True
        else:
            result += guess[i]

    if correct:
        print('You are correct!')
    else:
        print(f"There's no {guess_char} in the word.")
        turns -= 1

    return result, turns


def get_result(guess, answer, turns):
    """
    - If the guess is equal to answer => Win, return true to stop guessing
    - If turns = 0 => Lose, return true to stop guessing
    - Else => return False to keep going
    """
    if guess == answer:
        print('===========================')
        print('!!!!!!!!! You win !!!!!!!!!')
        print(f'The word was: {answer}')
        print('===========================')
        return True
    if turns == 0:
        print('===========================')
        print('You are completely hung :( ')
        print(f'The word was: {answer}')
        print('===========================')
        return True
    return False


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
