"""
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""
import random

MIN_NUM = -1000
MAX_NUM = 1000


def create_file(file_name, num_lines):
    with open(file_name, "w", encoding="U8") as file:
        for i in range(num_lines):
            print(
                f'{random.randint(MIN_NUM, MAX_NUM)} | '
                f'{random.random() * 2000 - 1000}',
                file=file)


if __name__ == "__main__":
    create_file("les07.txt", 10)
