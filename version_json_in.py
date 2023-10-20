import json
import random
import urllib.request


def get_elements_from_string(json_string):
    json_data = json.loads(json_string)
    return json_data


def all_numerations(json_data):
    for i in json_data:
        name_check = json_data[i]
        print(f"{i}. {name_check}")


def game_end(player_score, json_data, array_with_fail_answer):
    print(
        f"----------\nИгра окончена.\nПравильно отвеченные счета: {player_score}\nНеверно отвеченные счета: {json_data - player_score}\n")
    for i in array_with_fail_answer:
        print(i)
    print("----------")


def check_for_updates():
    remote_version_url = "https://raw.githubusercontent.com/Faunas/accountant_ticket_testing/master/version.txt"

    try:
        with urllib.request.urlopen(remote_version_url) as response:
            remote_version = response.read().decode("utf-8").strip()

            if remote_version != current_version:
                print(f"Доступна новая версия {remote_version}. Вы можете скачать её по ссылке.")
            else:
                print("У вас установлена последняя версия.")

    except Exception as e:
        print(f"Ошибка при проверке обновлений: {e}")


def start_gamemode_random(json_data):
    question_passed = 1
    player_score = 0
    all_data_old = len(json_data)
    array_with_fail_answer = []
    while json_data:
        random_key = random.choice(list(json_data.keys()))
        correct_answer = json_data[random_key]

        user_answer = input(f"Какой счёт относится к {random_key}?\nВаш ответ: ")

        if user_answer == correct_answer:
            print(f"Верно!\n{question_passed} / {all_data_old}")
            player_score += 1
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}\n{question_passed} / {all_data_old}")
            array_with_fail_answer.append(correct_answer)
        json_data.pop(random_key, None)
        question_passed += 1
    game_end(player_score, all_data_old, array_with_fail_answer)


def start_gamemode_increase(json_data):
    counter_keys_in_json = len(json_data)
    player_score = 0
    array_with_fail_answer = []
    print(f"Всего будет {counter_keys_in_json} вопроса.\nОпрос будет проводиться с 01 по 99 счёт.")
    for i in json_data:
        correct_answer = json_data[i]
        user_answer = input(f"Какой счёт относится к {i}?\nВаш ответ: ")
        if user_answer == correct_answer:
            print("Верно!")
            player_score += 1
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}")
            array_with_fail_answer.append(correct_answer)
    game_end(player_score, counter_keys_in_json, array_with_fail_answer)


def start_gamemode_decrease(json_data):
    counter_keys_in_json = len(json_data)
    player_score = 0
    array_with_fail_answer = []
    print(f"Всего будет {counter_keys_in_json} вопроса.\nОпрос будет проводиться с 99 по 01 счёта.")

    while json_data:
        current_key, correct_answer = json_data.popitem()
        user_answer = input(f"Какой счёт относится к {current_key}?\nВаш ответ: ")

        if user_answer == correct_answer:
            print("Верно!")
            player_score += 1
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}")
            array_with_fail_answer.append(correct_answer)
    game_end(player_score, counter_keys_in_json, array_with_fail_answer)


def main_menu():
    json_data_string = '''
    {
      "01": "Основные средства",
      "02": "Амортизация основных средств",
      "03": "Доходные вложения в материальные ценности",
      "04": "Нематериальные активы",
      "05": "Амортизация нематериальных активов",
      "07": "Оборудование к установке",
      "08": "Вложения во внеоборотные активы",
      "09": "Отложенные налоговые активы",
      "10": "Материалы",
      "11": "Животные на выращивании и откорме",
      "14": "Резервы под снижение стоимости материальных ценностей",
      "15": "Заготовление и приобретение материальных ценностей",
      "16": "Отклонение в стоимости материальных ценностей",
      "19": "Налог на добавленную стоимость по приобретенным ценностям",
      "20": "Основное производство",
      "21": "Полуфабрикаты собственного производства",
      "23": "Вспомогательные производства",
      "25": "Общепроизводственные расходы",
      "26": "Общехозяйственные расходы",
      "28": "Брак в производстве",
      "29": "Обслуживающие производства и хозяйства",
      "40": "Выпуск продукции (работ, услуг)",
      "41": "Товары",
      "42": "Торговая наценка",
      "43": "Готовая продукция",
      "44": "Расходы на продажу",
      "45": "Товары отгруженные",
      "46": "Выполненные этапы по незавершенным работам",
      "50": "Касса",
      "51": "Расчетные счета",
      "52": "Валютные счета",
      "55": "Специальные счета в банках",
      "57": "Переводы в пути",
      "58": "Финансовые вложения",
      "59": "Резервы под обесценение финансовых вложений",
      "60": "Расчеты с поставщиками и подрядчиками",
      "62": "Расчеты с покупателями и заказчиками",
      "63": "Резервы по сомнительным долгам",
      "66": "Расчеты по краткосрочным кредитам и займам",
      "67": "Расчеты по долгосрочным кредитам и займам",
      "68": "Расчеты по налогам и сборам",
      "69": "Расчеты по социальному страхованию и обеспечению",
      "70": "Расчеты с персоналом по оплате труда",
      "71": "Расчеты с подотчетными лицами",
      "73": "Расчеты с персоналом по прочим операциям",
      "75": "Расчеты с учредителями",
      "76": "Расчеты с разными дебиторами и кредиторами",
      "77": "Отложенные налоговые обязательства",
      "79": "Внутрихозяйственные расчеты",
      "80": "Уставный капитал",
      "81": "Собственные акции (доли)",
      "82": "Резервный капитал",
      "83": "Добавочный капитал",
      "84": "Нераспределенная прибыль (непокрытый убыток)",
      "86": "Целевое финансирование",
      "90": "Продажи",
      "91": "Прочие доходы и расходы",
      "94": "Недостачи и потери от порчи ценностей",
      "96": "Резервы предстоящих расходов",
      "97": "Расходы будущих периодов",
      "98": "Доходы будущих периодов",
      "99": "Прибыли и убытки"
    }
    '''

    json_iknow = '''
    {
      "01": "Основные средства",
      "02": "Амортизация основных средств",
      "03": "Доходные вложения в материальные ценности",
      "04": "Нематериальные активы",
      "05": "Амортизация нематериальных активов",
      "10": "Материалы",
      "11": "Животные на выращивании и откорме",
      "20": "Основное производство",
      "41": "Товары",
      "50": "Касса",
      "51": "Расчетные счета",
      "52": "Валютные счета",
      "55": "Специальные счета в банках",
      "80": "Уставный капитал",
      "90": "Продажи"
    }
    '''
    json_data = get_elements_from_string(json_data_string)
    json_iknow_strf = get_elements_from_string(json_iknow)

    print("\nТЕСТ НА ЗНАНИЕ БУХГАЛТЕРСКИХ СЧЕТОВ\n\nНеобходимо выбрать режим подготовки:\n"
          "[1] Вывести список всех счетов\n"
          "[2] Начать подготовку с рандомными счетами\n"
          "[3] Начать подготовку с счетами по возрастанию\n"
          "[4] Начать подготовку с счетами по убыванию\n"
          "[5] Повторить точно выученные счета\n")
    try:
        choose = int(input("Введите цифру для выбора соответствующего пункта: "))
    except Exception:
        print("Введены некорректные символы!")
        main_menu()
    if choose == 1:
        all_numerations(json_data)
    elif choose == 2:
        start_gamemode_random(json_data)
    elif choose == 3:
        start_gamemode_increase(json_data)
    elif choose == 4:
        start_gamemode_decrease(json_data)
    elif choose == 5:
        start_gamemode_random(json_iknow_strf)
    else:
        print("Введена неизвестная цифра! Повторяю информацию...")


if __name__ == "__main__":
    current_version = "1.0"
    while True:
        check_for_updates()
        main_menu()