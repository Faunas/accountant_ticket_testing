import json
import random


def get_elements_from_file(file_path):
    with open(file_path, 'r', encoding="UTF8") as file:
        json_data = json.load(file)
    return json_data


def all_numerations():
    file_path = 'all_numeration.json'
    with open(file_path, 'r', encoding="UTF8") as file:
        json_data = json.load(file)

    for i in json_data:
        name_check = json_data[i]
        print(f"{i}. {name_check}")


def main_menu():
    print("\nТЕСТ НА ЗНАНИЕ БУХГАЛТЕРСКИХ СЧЕТОВ\n\nНеобходимо выбрать режим подготовки:\n"
          "[1] Вывести список всех счетов\n"
          "[2] Начать подготовку с рандомными счетами\n"
          "[3] Начать подготовку с счетами по возрастанию\n")
    choose = int(input("Введите цифру для выбора соответствующего пункта: "))
    if choose == 1:
        all_numerations()
    elif choose == 2:
        start_gamemode_random()
    elif choose == 3:
        start_gamemode_increase()
    else:
        print("Введена неизвестная цифра! Повторяю информацию...")


def start_gamemode_random():
    file_path = 'all_numeration.json'
    json_data = get_elements_from_file(file_path)

    while True:
        random_key = random.choice(list(json_data.keys()))
        correct_answer = json_data[random_key]

        user_answer = input(f"Какой счёт относится к {random_key}?\nВаш ответ: ")

        if user_answer == correct_answer:
            print("Верно!")
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}")


def start_gamemode_increase():
    file_path = 'all_numeration.json'
    json_data = get_elements_from_file(file_path)

    counter_keys_in_json = len(json_data)
    player_score = 0
    player_fails = 0
    print(f"Всего будет {counter_keys_in_json} вопроса.\nОпрос будет проводиться от 01 до 99 счёта.")
    for i in json_data:
        correct_answer = json_data[i]
        user_answer = input(f"Какой счёт относится к {i}?\nВаш ответ: ")
        if user_answer == correct_answer:
            print("Верно!")
            player_score += 1
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}")
            player_fails += 1
    print(f"Игра окончена.\nПравильно отвеченные счета: {player_score}\nНеверно отвеченные счета: {len(json_data)-player_score}")


if __name__ == "__main__":
    while True:
        main_menu()
