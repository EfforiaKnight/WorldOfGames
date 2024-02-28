import os

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 42


def screen_cleaner():
    clear_cmd = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)
