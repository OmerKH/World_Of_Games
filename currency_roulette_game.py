import requests
from random import randrange

# the function needs to give a random number (generate_number)
# display it
# the user writes how much is the exchange rate (get_guess_from_user)
# compare between the guessing and the actual converted number (compare_results)
# see if it in the range
# return True or False


def generate_number():
    secret_number = randrange(101)
    return secret_number


def get_money_interval(sec_num):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url, timeout=10)
    # Validation for request
    if response.status_code == 200:
        data = response.json()

        ils_usd = data['rates']['ILS']
        converter = sec_num * ils_usd

        return converter
    else:
        print("Something went wrong")


# print(get_money_interval())


def get_guess_from_user(number):
    while True:
        try:
            guess_num = float(
                input(f"Enter you're guess, how much is {number} in ILS: "))
            if not isinstance(guess_num, float) or guess_num <= 0:
                print("Invalid input, Please try a positive number")
            else:
                return guess_num
        except ValueError:
            print("Invalid input")


def compare_results(secret_number, user_guess, difficulty):
    spectrum = 10 - difficulty
    max_range = secret_number + spectrum
    min_range = secret_number - spectrum
    return min_range <= user_guess <= max_range <= max_range

# print(compare_results(10, 1))


def play(difficulty):
    s_n = generate_number()
    if s_n is None:
        return "Something went wrong. Please try again."

    converted = get_money_interval(s_n)
    if converted is None:
        return "Failed to retrieve exchange rate :("

    y_n = get_guess_from_user(s_n)
    if compare_results(converted, y_n, difficulty):
        return True
    else:
        return f"You guessed {y_n} and it's not closed enough to {converted}"

