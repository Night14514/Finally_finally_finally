"""Utility functions."""
from datetime import datetime


def time_now() -> None:
    """Print current time if user inputs a single digit."""
    current_time = datetime.now()
    try:
        user_input = int(input("введите любую цифру: "))
        if user_input in range(10):
            print(f"сейчас: {current_time}")
    except ValueError:
        print("это не цифра")