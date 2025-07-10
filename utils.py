from json import load
from typing import Optional


def download_file(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = file.read().split()
    except Exception as e:
        print(f"Возникла ошибка при обработке файла: {e}")
        return []
    
    return words

def read_json(path: str) -> Optional[dict]:
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return load(file)
    except Exception as e:
        print(f"Возникла ошибка при чтении файла: {e}")
        return None
