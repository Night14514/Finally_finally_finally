import json
from typing import Any, Optional

JSON_PATH = "data.json"
OUTPUT_PATH = "output.txt"


def load_json(path: str) -> Optional[Any]:
    """Load JSON data from a file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("загрузка успешна")
        return data
    except json.JSONDecodeError:
        print("файл пустой или содержит некорректный json")
        return None
    except FileNotFoundError:
        print("файл не найден")
        return None


def save_json(data: Any, path: str) -> None:
    """Save data to a file in JSON format."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    print(f"данные сохранены в: {path}")


def search(key: str, path: str = OUTPUT_PATH) -> None:
    """Search for a key in the output file."""
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

if __name__ == "__main__":
    data = load_json(JSON_PATH)
    if data is not None:
        print(f"количество элементов в файле: {len(data)}")
        save_json(data, OUTPUT_PATH)
        key = input("введите ключ для поиска: ")
        search(key)