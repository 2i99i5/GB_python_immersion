"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь
до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
расширение файла.
"""
from os import path


def tuple_path(path_str: str) -> tuple:
    *path_list, file_name = path_str.split('\\')
    return ('\\'.join(path_list),  # в выводе двойной слэш, но если вывести как
            # элемент [0], то все в порядке
            file_name.split('.')[-2],
            file_name.split('.')[-1])


def tuple_path_os(path_str: str) -> tuple:
    path_, file_name = path.split(path_str)
    return (path_,
            file_name.split('.')[-2],
            file_name.split('.')[-1])


path_str = "D:\Projects\python_advanced\main.py"
print(tuple_path(path_str))

print(tuple_path_os(path_str))
