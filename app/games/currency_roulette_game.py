import math
import random
from dataclasses import dataclass

from currency_converter import CurrencyConverter

from app.games.base_game import GameResult, GameStatus, Game
from app.prompts import get_number, get_currency_number


@dataclass
class CurrencyGameResult(GameResult):
    currency_number: int


@dataclass
class CurrencyGameStatus(GameStatus):
    actual: CurrencyGameResult
    guess: CurrencyGameResult
    acceptable_diff: int

    def is_won(self) -> bool:
        return abs(self.guess.currency_number - self.actual.currency_number) <= self.acceptable_diff


class CurrencyGame(Game):
    BASE_ERROR: int = 10

    def __init__(self, difficulty: int) -> None:
        self._difficulty = difficulty
        self._usd = random.randint(1, 101)

    # noinspection PyMethodMayBeStatic
    def _get_game_status(self, actual: CurrencyGameResult, guess: CurrencyGameResult) -> CurrencyGameStatus:
        acceptable_diff = self.BASE_ERROR - self._difficulty
        return CurrencyGameStatus(actual, guess, acceptable_diff=acceptable_diff)

    def _generate_compare_result(self) -> GameResult:
        ils = convert_usd_to_ils(self._usd)
        return CurrencyGameResult(currency_number=ils)

    def _get_guess_from_user(self) -> GameResult:
        return CurrencyGameResult(currency_number=get_currency_number(self._usd))


def convert_usd_to_ils(usd: int) -> int:
    c = CurrencyConverter()
    return int(c.convert(usd, "USD", "ILS"))
