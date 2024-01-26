"""
Создайте функцию для сортировки файлов по директориям: видео, изображения,
текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для
сортировки.
"""

from create_06 import create_files
from os import path, mkdir, listdir, rename


def sort_files(type_dict: dict):
    for folder, value in type_dict.items():
        if folder:
            if not path.isdir(folder):
                mkdir(folder)
        file_list = []
        for file in listdir():
            ext = file.split(".")[-1]
            if ext in value:
                file_list.append(file)
        for file in file_list:
            new_file = f'{folder}/{file}'
            rename(file, new_file)


if __name__ == "__main__":
    type_dict = {
        'audio': ('rnd', 'txt'),
        'video': ('do', 'tx')
    }

    sort_files(type_dict)
