"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке
терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.
"""
from random import randint
from sys import argv


__all__ = ['game']

def game(count=10, start=1, stop=100):
    number = randint(start, stop)
    while count > 0:
        input_num = int(input(f"Введите число от {start} до {stop}: "))
        count -= 1
        if input_num < number:
            print("Больше ")
        elif input_num > number:
            print("Меньше ")
        else:
            return True
    return False


if __name__ == "__main__":
    if len(argv) == 2:
        if game(int(argv[1])):
            print("Ура, вы победили!")
        else:
            print("Повезет в следующий раз!")
    if len(argv) == 3:
        if game(int(argv[1]), int(argv[2])):
            print("Ура, вы победили!")
        else:
            print("Повезет в следующий раз!")
    if len(argv) == 4:
        if game(int(argv[1]), int(argv[2]), int(argv[3])):
            print("Ура, вы победили!")
        else:
            print("Повезет в следующий раз!")
