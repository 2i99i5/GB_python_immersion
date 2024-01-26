"""
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными
буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и
произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном
файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
from typing import TextIO


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def combine():
    with open("names.txt", "r", encoding="U8") as file_names, \
            open("les07.txt", "r", encoding="U8") as file_numbers, \
            open("result.txt", "w", encoding="U8") as file_result:
        len_names = sum(1 for _ in file_names)
        len_numbers = sum(1 for _ in file_numbers)
        for _ in range(max(len_names, len_numbers)):
            name = read_line_or_begin(file_names)
            num1, num2 = read_line_or_begin(file_numbers).split(" | ")
            num1 = int(num1)
            num2 = float(num2)
            num = num1 * num2
            if num < 0:
                name = name.lower()
                num = abs(num)
            else:
                name = name.upper()
                num = round(num)
            print(f"{name}\t{num}", file=file_result)


if __name__ == "__main__":
    combine()
