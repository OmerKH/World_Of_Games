from random import randrange


# generate_number():
# takes a random number === import random
# save it as secret_number

def generate_number(difficulty):
    if not isinstance(difficulty, int) or difficulty < 0:
        print("Please enter a number from 0 to 10")
        return None
    secret_number = randrange(difficulty)
    return secret_number

###
# get_guess_from_user :
# input - int()  <-- validation!!
#


def get_guess_from_user(difficulty):
    while True:
        try:
            guess_num = int(
                input("input a number between 0 to the difficulty level: "))
            if 0 <= guess_num <= difficulty:
                return guess_num
            else:
                print("Invalid input, Please try a number between 0 to 10")
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


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
