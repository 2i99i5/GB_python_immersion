"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в
ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle

__all__ = ['get_size', 'dir_walker', 'save_to_csv', 'save_to_picle',
           'save_to_json']

COLUMN_PARENT = 'parent'
COLUMN_TYPE = 'is_file'
COLUMN_NAME = 'filename'
COLUMN_SIZE = 'size'
OUTPUT_NAME = 'output'


def get_size(path: str) -> int:
    size = 0
    for dirpaths, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpaths, f)
            size += os.path.getsize(fp)
    return size


def dir_walker(dir_path: str):
    results = []
    for dirpaths, dirnames, filenames in os.walk(dir_path):
        for name in filenames:
            full_path = os.path.join(dirpaths, name)
            results.append({COLUMN_PARENT: dirpaths,
                            COLUMN_TYPE: True,
                            COLUMN_NAME: name,
                            COLUMN_SIZE: os.path.getsize(full_path)})

        for name in dirnames:
            full_path = os.path.join(dirpaths, name)
            results.append({COLUMN_PARENT: dirpaths,
                            COLUMN_TYPE: False,
                            COLUMN_NAME: name,
                            COLUMN_SIZE: get_size(full_path)})

    save_to_csv(results, f'{OUTPUT_NAME}.csv')
    save_to_json(results, f'{OUTPUT_NAME}.json')
    save_to_picle(results, f'{OUTPUT_NAME}.pickle')


def save_to_csv(data: list, file_name: str):
    with open(file_name, "w", encoding="UTF-8", newline='') as f:
        csw_writer = csv.DictWriter(f,
                                    dialect='excel',
                                    quoting=csv.QUOTE_MINIMAL,
                                    fieldnames=data[0].keys()
                                    )
        csw_writer.writeheader()
        csw_writer.writerows(data)


def save_to_json(data: list, file_name: str):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


def save_to_picle(data: list, file_name: str):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)


if __name__ == "__main__":
    dir_walker("./01")
