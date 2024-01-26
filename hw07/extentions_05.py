"""
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""

from gen_files_04 import create_files


def generate_file_with_ext(ext_dict: dict):
    for key, value in ext_dict.items():
        create_files(key, num=value)


if __name__ == "__main__":
    ext_dict = {
        "tx": 2,
        "do": 4,
    }
    generate_file_with_ext(ext_dict)
