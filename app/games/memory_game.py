import random
from dataclasses import dataclass
from typing import List

from app.games.base_game import GameResult, GameStatus, Game
from app.prompts import get_number, show_numbers, get_numbers


@dataclass
class MemoryGameResult(GameResult):
    numbers: List[int]


class MemoryGameStatus(GameStatus):
    def is_won(self) -> bool:
        return self.actual == self.guess


class MemoryGame(Game):
    def __init__(self, difficulty: int) -> None:
        self._difficulty = difficulty

    # noinspection PyMethodMayBeStatic
    def _get_game_status(self, actual: GameResult, guess: GameResult) -> GameStatus:
        return MemoryGameStatus(actual, guess)

    def _generate_compare_result(self) -> GameResult:
        numbers = [random.randint(0, 101) for _ in range(self._difficulty)]
        show_numbers(numbers)
        return MemoryGameResult(numbers=numbers)

    def _get_guess_from_user(self) -> GameResult:
        return MemoryGameResult(numbers=get_numbers(self._difficulty))
