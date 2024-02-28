import time
from typing import List

from rich.prompt import IntPrompt

from app import console
from app.prompts import delete_line


def show_numbers(numbers: List[int]) -> None:
    console.print("Remember those numbers: ")
    console.print(numbers)
    time.sleep(0.7)
    delete_line()


def get_numbers(count: int) -> List[int]:
    console.print("Enter numbers you saw one by one (click enter between numbers)")
    return [IntPrompt.ask(console=console) for _ in range(count)]
