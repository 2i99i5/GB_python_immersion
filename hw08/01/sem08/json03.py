"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в
формате CSV.
"""

import csv
import json


def save_csv():
    with open("ids.json", "r", encoding='utf8') as file_json:
        data = json.load(file_json)
    with open("ids.csv", 'w', encoding='utf8') as file_csv:
        for level, value in data.items():
            for idx, name in value.items():
                print(f'{level},{idx},{name}', file=file_csv)

if __name__ == "__main__":
    save_csv()
