"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
import random

MIN_LEN = 4
MAX_LEN = 7
MIN_ORD = ord('a')
MAX_ORD = ord('z')
VOWELS = {"a", "o", "u", "e", "i", "y"}


def gen_names():
    length = random.randint(MIN_LEN, MAX_LEN)
    name = ''
    for i in range(length):
        name += chr(random.randint(MIN_ORD, MAX_ORD))
    for char in name:
        if char in VOWELS or char.lower() in VOWELS:
            break
    else:
        ind = random.randint(0, len(name) - 1)
        letter = random.choice(list(VOWELS))

        name = name[:ind] + letter + \
               (name[ind + 1:] if ind < len(name) - 1 else "")

    return name


if __name__ == "__main__":
    with open("names.txt", "w", encoding="U8") as file:
        for i in range(10):
            print(gen_names(), file=file)
