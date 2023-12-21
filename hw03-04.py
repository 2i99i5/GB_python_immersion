# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def subsets(list_set: list) -> list:
    # возвращает все возможные "подмножества" исходного "множества"
    sets = []
    len_list = len(list_set)
    for i in range(1 << len_list):
        subset = [list_set[bit] for bit in range(len_list) if i & (1 << bit)]
        sets.append(subset)
    return sets


tools = {
    'спички': 1,
    'нож': 2,
    'надувной круг': 7,
    'носки': 2,
    'котелок': 3,
    'палки для хотьбы': 8,
    'веревка': 3,
    'купальник': 2,
    'бельё': 2,
    'куртка': 3,
    'тапочки': 3,
    'спальник': 8,
    'матрац': 3,
    'палатка': 12,
    'тушенка': 2,
    'горелка': 3,
    'провизия': 8
}

# для наглядности лучше или малые значения (1-3), или 70+
max_capacity = int(input('Введите вместительность рюкзака: '))

tools_list = list(tools)  # из ключей делаю список
dict_combination = {}

# создаю словарь со всеми комбинациями и их весом
for combination in subsets(tools_list):
    tuple_combintion = tuple(combination)
    for tool in tuple_combintion:
        weight = tools.get(tool, 0)
        if tuple_combintion not in dict_combination:
            dict_combination[tuple_combintion] = weight
        else:
            dict_combination[tuple_combintion] += weight

# вывожу компбинации, вес которых равен заданному
for key, value in dict_combination.items():
    if value == max_capacity:
        # <= max_capacity: если учесть, что можно рюкзак не заполнять на 100%
        print(key)
