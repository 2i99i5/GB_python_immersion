# 2. Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    res_dict = {}
    for value, key in kwargs.items():
        if isinstance(key, list | dict | set | bytearray):  # from python 3.10
            key = str(key)
        res_dict[key] = value
    return res_dict


print(create_dict(tuple_1=('a', 1), list_2=[1, 0], num3=256, str4="hello"))
