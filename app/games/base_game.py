from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Protocol


class GameResult:
    pass


@dataclass
class GameStatus(ABC):
    actual: GameResult
    guess: GameResult

    @abstractmethod
    def is_won(self) -> bool:
        pass


class Game(ABC):
    def play(self) -> bool:
        actual = self._generate_compare_result()
        guess = self._get_guess_from_user()
        game_status = self._get_game_status(actual, guess)

        return game_status.is_won()

    @abstractmethod
    def _get_game_status(self, actual: GameResult, guess: GameResult) -> GameStatus:
        pass

    @abstractmethod
    def _generate_compare_result(self) -> GameResult:
        pass

    @abstractmethod
    def _get_guess_from_user(self) -> GameResult:
        pass
