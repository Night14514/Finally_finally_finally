from datetime import datetime


def time_now() -> None:
    current_time = datetime.now()
    try:
        user_input = int(input("введите любую цифру: "))
        if user_input in range(10):
            print("сейчас: ", current_time)
    except ValueError:
        print("это не цифра")