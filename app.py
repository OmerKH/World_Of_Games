#                                                 World of Games project                                              #
from games.guess_game import play as start_guess_game
from games.memory_game import play as start_memory_game
from games.currency_roulette_game import play as start_currency_roulette_game
from score import add_score


def welcome():
    while True:
        user_name = input("Enter your name (or type 'exit' to quit): ").strip()
        if user_name.lower() in ["exit", "quit"]:
            print("Exiting the program. Goodbye!")
            exit()
        elif user_name:
            return f"Hi {user_name} and welcome to the World of Games: The Epic Journey"
        else:
            print("Name cannot be empty. Please enter a valid name.")


# list of games.
# if statement to choose the right game
# difficulty to choose from
def start_play():
    game_list = ["Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
                 "Guess Game - guess a number and see if you chose like the computer.",
                 "Currency Roulette - try and guess the value of a random amount of USD in ILS "]

    # Validation of selection
    while True:
        while True:
            try:
                options = int(input("""Pick a game (1) Memory Game 
                (2) Guess Game 
                (3) Currency Roulette
                --> """))
                if 1 <= options <= 3:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"You picked {game_list[options - 1]} Enjoy!")

        while True:
            try:
                difficulty = int(
                    input("Choose the level of difficulty you would like to play with from 1 - 5 :"))
                if 1 <= difficulty <= 5:
                    break
                else:
                    print(
                        "Invalid difficulty level. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"You chose to play with difficulty level {
            difficulty} I wish you good luck!")
        while True:
            if options == 1:
                result = start_memory_game(difficulty)
            elif options == 2:
                result = start_guess_game(difficulty)
            elif options == 3:
                result = start_currency_roulette_game(difficulty)

            if result is True:
                score = add_score(difficulty)
                print(f"You won! your score is now {score}")
            else:
                try:
                    score = int(
                        open("Scores.txt", "r", encoding="utf-8").read().strip())
                    print(f"Sorry, you lost your score is {score}")
                except FileNotFoundError:
                    print("Sorry, you lost. You don't have a score yet.")

            print(result)

            play_again = input(
                "Do you want to play again? (yes/no): ").strip().lower()
            if play_again not in ["yes", "y"]:
                break

        another_game = input(
            "Do you want to choose another game? (yes/no): ").strip().lower()
        if another_game not in ["yes", "y"]:
            print("Thank you for playing! Goodbye!")
            with open("Scores.txt", "w", encoding="utf-8") as file:
                file.write("0")
            break


#
# welcome()
# start_play()

welcome_message = welcome()
if welcome_message:
    print(welcome_message)
    start_play()
else:
    print("Exiting the program. Please restart and enter a valid name.")
