"""Utility functions."""
from datetime import datetime


class TimeUtility:
    """Handles time-related utility operations."""

    def display_current_time(self) -> None:
        """Print current time if user inputs a single digit."""
        try:
            user_input = int(input("введите любую цифру: "))
            if user_input in range(10):
                current_time = datetime.now()
                print(f"сейчас: {current_time}")
            else:
                print("это не цифра, а число")
        except ValueError:
            print("это не цифра")