import os

SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = "707"

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


