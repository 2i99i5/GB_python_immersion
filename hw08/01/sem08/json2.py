"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный
идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
import os


def ask_id(data: dict):
    with open("ids.json", 'w', encoding='utf8') as file:
        while True:
            try:

                ask_id = input('Введите идентификатор: ')
                if not ask_id.isdigit():
                    raise Exception
            except:
                break
            name = input("Введите имя: ")
            level = input('Введите уровень доступа: ')
            if int(level) not in range(1, 8):
                print('Неверный уровень доступа')
                continue
            for lvl in data:
                if ask_id in data[lvl]:
                    print("Неверный идентификатор.")
                    continue
            data[level][ask_id] = name
        json.dump(data, file, ensure_ascii=False, indent=4)
    return data


if __name__ == "__main__":
    if os.path.exists("ids.json"):
        with open("ids.json", 'r', encoding='utf8') as file:
            data = json.load(file)
            print(data)
    else:
        data = {str(i): {} for i in range(1, 8)}

    data = ask_id(data)
