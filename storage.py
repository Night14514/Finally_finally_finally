import json
from typing import Any, Optional


def load_json(path: str) -> Optional[Any]:
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
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    print(f"данные сохранены в: {path}")