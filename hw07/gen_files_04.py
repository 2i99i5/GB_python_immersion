"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import random

MIN_NAME_LEN = 6
MAX_NAME_LEN = 30
MIN_FILE_LEN = 256
MAX_FILE_LEN = 4096
NUM_FILES = 2
MIN_ORD = ord('a')
MAX_ORD = ord('z')

def generate_name(min_len=MIN_NAME_LEN,
                 max_len=MAX_NAME_LEN):
    length = random.randint(min_len,max_len)
    name = []
    for i in range(length):
        name.append(chr(random.randint(MIN_ORD, MAX_ORD)))
    return "".join(name)

def create_files(ext,
                 min_len=MIN_NAME_LEN,
                 max_len=MAX_NAME_LEN,
                 min_file=MIN_FILE_LEN,
                 max_file=MAX_FILE_LEN,
                 num=NUM_FILES
                 ):
   for i in range(num):
       name = generate_name(min_len,max_len)
       length = random.randint(min_file,max_file)
       text = []
       with open(f"{name}.{ext}", "w", encoding="U8") as text_file:
           for j in range(length):
               text.append(chr(random.randint(MIN_ORD, MAX_ORD)))
           print(''.join(text), file=text_file)


if __name__ == "__main__":
    create_files("rnd")
