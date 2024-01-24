"""
Добавьте в модуль с загадками функцию, которая принимает на вход строку
(текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого
словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
"""

from dict_riddle import riddle_dict

_riddle_dict = {}


def agr_results(riddle, count):
    if riddle not in _riddle_dict:
        _riddle_dict[riddle] = []
    _riddle_dict[riddle].append(count)


def print_results():
    for key, value in _riddle_dict.items():
        print(f'Загадка: {key} \n Угадана с {value[0]} попытки')


if __name__ == "__main__":
    rd = riddle_dict()
    for riddle, count in rd:
        agr_results(riddle, count)
    print_results()
