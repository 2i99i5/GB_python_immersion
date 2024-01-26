"""
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import random
from os import path, mkdir

MIN_NAME_LEN = 6
MAX_NAME_LEN = 30
MIN_FILE_LEN = 256
MAX_FILE_LEN = 4096
NUM_FILES = 2
MIN_ORD = ord('a')
MAX_ORD = ord('z')


def generate_name(min_len=MIN_NAME_LEN,
                  max_len=MAX_NAME_LEN):
    length = random.randint(min_len, max_len)
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_ORD, MAX_ORD)))
    return "".join(name)


def create_files(ext,
                 folder='',
                 min_len=MIN_NAME_LEN,
                 max_len=MAX_NAME_LEN,
                 min_file=MIN_FILE_LEN,
                 max_file=MAX_FILE_LEN,
                 num=NUM_FILES
                 ):
    for i in range(num):
        name = generate_name(min_len, max_len)
        length = random.randint(min_file, max_file)
        text = []
        if folder:
            if not path.isdir(folder):
                mkdir(folder)
            name = f'{folder}/{name}'
        try:
            with open(f"{name}.{ext}", "x", encoding="U8") as text_file:
                for j in range(length):
                    text.append(chr(random.randint(MIN_ORD, MAX_ORD)))
                print(''.join(text), file=text_file)
        except:
            pass


if __name__ == "__main__":
    create_files(ext="gol", folder='result')
