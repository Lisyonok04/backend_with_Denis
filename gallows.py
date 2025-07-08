import random

from auxiliary_functions import downloading_from_file, read_json
from all_consts import ALPHA, MAX_ERRORS, JSON_WAY


def drawing(gallow_path:str, errors: int) -> str:
    gallow_draw = read_json(gallow_path)
    return gallow_draw[str(errors)]
    

def guessing(words: list[str]) -> None:
    word = random.choice(words)
    guessed = ["_"] * len(word)
    errors = 0
    used = []

    while True:
        print("\nСлово:", " ".join(guessed))
        print(drawing(JSON_WAY, errors))

        if "_" not in guessed:
            print("Поздравляем! Вы угадали слово!")
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
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
        else:
            errors += 1
            print("Такой буквы нет в загаданном слове. Осталось попыток:", MAX_ERRORS - errors)
        print("Использованные буквы: ", used)

while True:
    words = downloading_from_file("words.txt")
    print("1. Начать новую игру")
    print("2. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        guessing(words)
    elif choice == "2":
        print("Спасибо за игру! До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
