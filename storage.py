"""Storage operations."""
import json
from typing import Any, Optional


class JsonStorage:
    """Handles JSON file storage operations."""

    def load(self, path: str) -> Optional[Any]:
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

    def save(self, data: Any, path: str) -> None:
        """Save data to a file in JSON format."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"данные сохранены в: {path}")