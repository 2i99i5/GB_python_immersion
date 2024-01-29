"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

"""

import pickle
import csv

def pickle_to_csv():
    with open('new_ids.pickle', 'rb') as file_pickle:
        data = pickle.load(file=file_pickle)
    with open('new_ids.csv', 'w', encoding='u8') as file_csv:
        print(type(data))
        for line in data:
            print(line)
            for key1, value1 in line.items():
                for key2, value2 in value1.items():
                    print(key1, key2, value2, sep=',', file=file_csv)


if __name__ == "__main__":
    pickle_to_csv()

"homework pathlib"

import os
import csv
import json
import pickle


def structure_of_directory(dir):
    dict = {}
    os.chdir(dir)
    for file in os.listdir(f'D:\Geek\Python_final\{dir}'):
        file_size = os.path.getsize(f'D:\Geek\Python_final\{dir}/' + file)
        dict[file] = [os.getcwd(), 'f', file_size]
    for _, dir_name, file_name in os.walk(os.getcwd()):
        # print(f'{dir_name = }\n{file_name = }\n')

        for directory in dir_name:
            # print(directory)
            size = 0
            for file in os.listdir(directory):
                file_size = os.path.getsize(directory + '/' + file)
                dict[file] = [directory, 'f', file_size]
                size += file_size
            dict[directory] = [os.getcwd(), 'd', size]
    with open('test.json', 'w', encoding='UTF-8') as f1:
        json.dump(dict, f1, ensure_ascii=False)


def json_to_csv(name):
    new_name = name.split('.')[0]
    csv_file_name = new_name + '.csv'
    with open(name, encoding='UTF-8') as f1, \
            open(csv_file_name, 'w', newline='', encoding='UTF-8') as f2:
        data = json.load(f1)
        rows = []
        for name, value in data.items():
            directory, type_f, size_f = value
            rows.append({'directory': directory, 'type': type_f, 'size_f': int(size_f), 'name': name})
        csv_write = csv.DictWriter(f2, fieldnames=['directory', 'type', 'size_f', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


def json_to_pickle(name):
    new_name = name.split('.')[0]
    pickle_file_name = new_name + '.pickle'
    # print(pickle_file_name)
    with open(name, 'r', encoding='UTF-8') as f1:
        with open(pickle_file_name, 'wb') as f2:
            data = json.load(f1)
            pickle.dump(data, f2)


structure_of_directory('Testdir')
json_to_csv('test.json')
json_to_pickle('test.json')