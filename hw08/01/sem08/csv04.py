"""
Прочитайте созданный в прошлом задании csv файл без использования
csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла
представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import json


def csv_to_json(file_csv_name, file_json_name):
    with open(file_csv_name + '.csv', 'r', encoding='u8') as file_csv:
        data = []
        for line in file_csv:
            level, idx, name = line.strip().split(',')
            idx = f'{int(idx):010d}'
            name = name.capitalize()
            hashx = hash(name + idx)
            data.append({level: [idx, name, hashx]})
    with open(file_json_name + '.json', 'w', encoding='u8') as file_json:
        for line in data:
            json.dump(line, file_json, ensure_ascii=False)
            print(file=file_json)


if __name__ == "__main__":
    csv_to_json('ids', 'new_ids')
