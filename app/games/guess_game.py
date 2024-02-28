import random
from dataclasses import dataclass

from app.games.base_game import GameResult, GameStatus, Game
from app.prompts import get_number


@dataclass
class GuessGameResult(GameResult):
    number: int


class GuessGameStatus(GameStatus):
    def is_won(self) -> bool:
        return self.actual == self.guess


class GuessGame(Game):
    def __init__(self, difficulty: int) -> None:
        self._difficulty = difficulty

    # noinspection PyMethodMayBeStatic
    def _get_game_status(self, actual: GameResult, guess: GameResult) -> GameStatus:
        return GuessGameStatus(actual, guess)

    def _generate_compare_result(self) -> GameResult:
        return GuessGameResult(number=random.randint(0, self._difficulty))

    def _get_guess_from_user(self) -> GameResult:
        return GuessGameResult(number=get_number(self._difficulty))
