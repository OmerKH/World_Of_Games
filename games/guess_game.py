from random import randrange
from utils.utils import validate_input, compare_values


# generate_number():
# takes a random number === import random
# save it as secret_number

def generate_number(difficulty):
    if not isinstance(difficulty, int) or difficulty < 0:
        print("Please enter a number from 0 to 10")
        return None
    secret_number = randrange(difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    prompt = "Input a number between 0 to the difficulty level: "
    return validate_input(prompt, int, 0, difficulty)


def compare_results(secret_number, user_guess):
    return compare_values(secret_number, user_guess, "exact")


def play(difficulty):
    s_n = generate_number(difficulty)
    if s_n is None:
        return "Invalid difficulty level"

    y_n = get_guess_from_user(difficulty)

    if compare_results(s_n, y_n):
        return f"You guessed the {True} number"
    else:
        return f"Sorry, the correct number was {s_n}. Better luck next time!"


# print(play(3))
