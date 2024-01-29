"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с
псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в
формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json

with open("data.txt", "r", encoding="utf8") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].capitalize().strip()
with open("data.json", "w", encoding="utf8") as write_file:
    json.dump(data, write_file, indent=4, ensure_ascii=False)
