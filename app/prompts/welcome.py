from rich.prompt import Prompt
from app import console


def welcome():
    username = Prompt.ask("Please tell me your name", console=console)
    console.print(
        f"Hi [bold blue]{username}[/bold blue] and "
        f"welcome to the [bold blue]World of Games: The Epic Journey[/bold blue]"
    )
