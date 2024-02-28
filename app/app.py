from app.games import GuessGame, Game, MemoryGame, CurrencyGame
from app.prompts import get_game, game_status
from app.score import add_score


def game_factory(game_num: int, difficulty: int) -> Game:
    games = [
        MemoryGame(difficulty),
        GuessGame(difficulty),
        CurrencyGame(difficulty)
    ]

    return games[game_num-1]


def start_play():
    game_num, difficulty = get_game()
    game = game_factory(game_num, difficulty)
    is_won = game.play()

    if is_won:
        game_status.won()
        add_score(difficulty)
    else:
        game_status.lose()
