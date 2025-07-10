from json import load
from typing import Optional


def download_file(filename: str) -> Optional[list[str]]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = file.read().split()
    except FileNotFoundError as e:
        print(f"Возникла ошибка при обработке файла: {e}")
        return None
    if not words:
        print("Слов нет. Игры не будет")
        return None
    return words

def read_json(path: str) -> Optional[dict]:
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return load(file)
    except FileNotFoundError as e:
        print(f"Возникла ошибка при чтении файла: {e}")
        return None
