"""Search operations."""


def search(key: str, path: str) -> None:
    """Search for a key in a file."""
    if not key or key.isspace():
        raise ValueError("ошибка: пустой ключ")
    try:
        with open(path, "r", encoding="utf-8") as f:
            found = False
            for line in f:
                if key in line:
                    print(line.strip())
                    found = True

            if not found:
                print("ничего не найдено")
    except FileNotFoundError:
        print(f"файл {path} не найден")