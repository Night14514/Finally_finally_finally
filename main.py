"""Main application module."""
from config import JSON_PATH, OUTPUT_PATH
from search_ops import FileSearcher
from storage import JsonStorage
from utils import TimeUtility


def main() -> None:
    """Run the main application."""
    storage = JsonStorage()
    searcher = FileSearcher()
    time_util = TimeUtility()

    data = storage.load(JSON_PATH)
    if data is not None:
        print(f"количество элементов в файле: {len(data)}")
        storage.save(data, OUTPUT_PATH)
        key = input("введите ключ для поиска: ")
        try:
            searcher.search(key, OUTPUT_PATH)
        except ValueError as e:
            print(e)
        time_util.display_current_time()


if __name__ == "__main__":
    main()