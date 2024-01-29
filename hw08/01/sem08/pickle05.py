"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет
их содержимое в виде одноимённых pickle файлов.
"""

import os
import json
import pickle


def find_json(folder):
    for file in os.listdir(folder):
        print(file)
        file_name, extension = file.split('.')
        if extension == 'json':
            with open(f'{folder}/{file}', 'r', encoding="u8") as file_json:
                data = json.load(file_json)
                print(data)
            with open(f'{folder}/{file_name}.pickle', 'wb') as file_pickle:
                pickle.dump(str(data), file_pickle)


if __name__ == "__main__":
    find_json(os.getcwd())
