from rich.prompt import IntPrompt

from app import console


def get_number(limit: int) -> int:
    choices = map(str, range(0, limit))
    return IntPrompt.ask("Input a number", console=console, choices=list(choices))
