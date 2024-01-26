"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце
имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно
работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os
from os import listdir
from os.path import isfile, join


def file_renamer(
        name: str,  # конечное имя файлов
        digits_of_num: int,  # количество цифр в порядковом номере файла
        find_extension: str,  # расширение под замену
        final_extension: str,  # расширение выходных файлов
        from_name: int = 1,  # начало диапазона букв исходного файла
        to_name: int = 1  # конец диапазона букв исходного файла не включая
):
    count = 1
    onlyfiles = [
        f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))
    ]
    print(f'Список файлов в папке:\n{onlyfiles}')
    try:
        for file in onlyfiles:
            if file.split('.')[-1] == find_extension:
                file_name = file.split('.')[0][from_name - 1:to_name - 1]
                if len(str(count)) != digits_of_num:
                    tmp = (digits_of_num - len(str(count))) * '0'
                    file_count = (f'{tmp}{count}')

                final_name = (
                    f'{file_name}{name}{file_count}.{final_extension}')
                print(file, end=' -> ')
                os.rename(file, final_name)
                print(final_name)
                count += 1
    except:
        print('incorrect input parameters')


__all__ = ['file_renamer']

if __name__ == '__main__':
    file_renamer('hw_test_name', 3, 'jpg', 'png', 1, 3)
