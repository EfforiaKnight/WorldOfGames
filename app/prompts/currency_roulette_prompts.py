from rich.prompt import IntPrompt

from app import console


def get_currency_number(usd: int) -> int:
    return IntPrompt.ask(f"Guess the value of {usd} USD in ILS", console=console)
