'''
Steps:
Generate a random number between 1 and 100
Define two levels ie., easy and hard
For easy, 10 attemps. For hard, 5 attemps
'''
from art import logo
from random import randint
answer = randint(1, 100)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1  # decrement the turns by 1
    elif guess < answer:
        print("Too low.")
        return turns - 1  # decrement the turns by 1
    else:
        print(f"You got it! The answer was {answer}.")
        return

# Make function to set difficulty.


def set_difficulty():
    '''Returns the number of turns for each mode'''
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    answer = randint(1, 50)
    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.\n")
        # check_answer(guess, answer, turns)


# calling the game function to run the game
game()
