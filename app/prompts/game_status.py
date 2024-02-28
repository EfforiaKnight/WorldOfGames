from app import console


def won() -> None:
    console.print("You won! :sunglasses::1st_place_medal:", style="bold green", emoji=True)


def lose() -> None:
    console.print("You lose :upside-down_face:", style="bold red", emoji=True)
