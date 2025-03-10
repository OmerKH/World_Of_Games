# add_score(difficulty): reads the score from file Score_File
# than --> POINTS_OF_WINNING = (DIFFICULTY X 3) + 5 Each

from utils.utils import SCORES_FILE_NAME



def add_score(difficulty):
    # Method
    addition = (difficulty * 3) + 5

    # write to file Scores.txt
    try:
        with open(SCORES_FILE_NAME, "r", encoding="utf-8") as f:
            current_score = int(f.read().strip())
    except FileNotFoundError:
        current_score = 0

    current_score += addition

    with open(SCORES_FILE_NAME, "w", encoding="utf-8") as f:
        f.write(str(current_score))

    return current_score
