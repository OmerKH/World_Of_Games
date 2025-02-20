import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "707"


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_input(prompt, input_type, min_value=None, max_value=None):

    while True:
        try:
            user_input = input_type(input(prompt))
            if (min_value is None or user_input >= min_value) and \
               (max_value is None or user_input <= max_value):
                return user_input
            print(f"Input must be between {min_value} and {max_value}")
        except ValueError:
            print(f"Invalid input. Please enter a {input_type.__name__}")


def compare_values(value1, value2, comparison_type="exact", tolerance=0):

    if comparison_type == "exact":
        return value1 == value2
    elif comparison_type == "range":
        return abs(value1 - value2) <= tolerance
    elif comparison_type == "list":
        return value1 == value2
    return False
