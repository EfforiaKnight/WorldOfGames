from textwrap import dedent
from rich.prompt import IntPrompt

from app import console


def get_game():
    games_text = """
        Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back.
            2. Guess Game - guess a number and see if you chose like the computer.
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """

    console.print(dedent(games_text))
    game_num = IntPrompt.ask("Game number", console=console, choices=["1", "2", "3"])
    difficulty = IntPrompt.ask("Select game difficulty", console=console, choices=["1", "2", "3", "4", "5"])

    return game_num, difficulty
