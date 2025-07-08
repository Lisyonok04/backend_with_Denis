from json import load
from typing import Optional


def downloading_from_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
    if not words:
        raise ValueError("Файл слов пуст. Угадывать нечего...")
    return words

def read_json(path: str) -> Optional[dict]:
    with open(path, "r", encoding="UTF-8") as file:
        return load(file)
