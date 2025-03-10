import time
from random import randrange
import os
from utils import validate_input, compare_values


# the function needs to generate sequence of random numbers depending on the difficulty level (generate_sequence)
# display it for 0.7 sec
# the user writes the numbers which he remembers (get_list_from_user)
# compare between the guessing and the actual converted number (is_list_equal)
# return True or False


def generate_sequence(difficulty):
    if not isinstance(difficulty, int) or 0 >= difficulty > 10:
        print("Please enter a number from 0 to 10")
        return None

    memory_list = [randrange(1, 101) for numb in range(difficulty)]
    return memory_list

# print(generate_sequence(5))


def display_sequence(sequence, delay):
    if not isinstance(sequence, list) or not sequence:
        raise ValueError("Invalid sequence")

    print(sequence)
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

# display_sequence(generate_sequence(2),0.7)


def get_list_from_user(difficulty):
    guess_list = []
    for _ in range(difficulty):
        prompt = "Enter what you're remembering: "
        guess_num = validate_input(prompt, int, 1, 100)
        guess_list.append(guess_num)
    return guess_list


def is_list_equal(gen_list, user_list):
    return compare_values(gen_list, user_list, "list")


def play(difficulty):
    seq = generate_sequence(difficulty)
    if seq is None:
        return "Invalid difficulty level"

    display_sequence(seq, 0.7)

    user_guess = get_list_from_user(difficulty)

    if is_list_equal(seq, user_guess):
        return True
    else:
        return False
