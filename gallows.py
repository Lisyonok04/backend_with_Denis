import random

from utils import read_json, download_file
from all_consts import ALPHA, MAX_ERRORS, JSON_PATH, TXT_PATH
    

def guessing(words: list[str], gallow_draw: list[str]) -> None:
    word = random.choice(words)
    guessed = ["_"] * len(word)
    errors = 0
    used = []
    while True:
        print("\nСлово:", " ".join(guessed))
        print(gallow_draw[str(errors)])

        if "_" not in guessed:
            print("Поздравляю! Вы угадали слово!")
            break

        if errors >= MAX_ERRORS:
            print("Поздравляю, вас повесили! Загаданное слово было таким простым:", word)
            break

        letter = input("Введите букву: ").lower()
        while letter not in ALPHA:
            print("Пожалуйста, введите ОДНУ РУССКУЮ букву!")
            letter = input("Введите букву: ").lower()
        while letter in used:
            print("Вы уже использовали эту букву!")
            print("Использованные буквы: ", used)
            letter = input("Введите букву: ").lower()
        used.append(letter)
        in_word = False
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
                in_word = True
        if not in_word:
            errors += 1
            print("Такой буквы нет в загаданном слове. Осталось попыток:", MAX_ERRORS - errors)
        print("Использованные буквы: ", used)

def main() -> None:
    if not download_file(TXT_PATH) or not read_json(JSON_PATH):
        return
    words = download_file(TXT_PATH)
    gallow_draw = read_json(JSON_PATH)
    while True:
        print("1. Начать новую игру")
        print("2. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            guessing(words, gallow_draw)
        elif choice == "2":
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")