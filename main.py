from config import JSON_PATH, OUTPUT_PATH
from search_ops import search
from storage import load_json, save_json
from utils import time_now


def main() -> None:
    data = load_json(JSON_PATH)
    if data is not None:
        print(f"количество элементов в файле: {len(data)}")
        save_json(data, OUTPUT_PATH)
        key = input("введите ключ для поиска: ")
        try:
            search(key, OUTPUT_PATH)
        except ValueError as e:
            print(e)
        time_now()


if __name__ == "__main__":
    main()