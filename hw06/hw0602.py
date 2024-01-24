"""
3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
а если бьют - ложь.
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки
"""
import random

BOARD_SIZE = 8


def print_board(queens):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if queens[i][0] == i + 1 and queens[i][1] == j + 1:
                print(f'X ', end='')
            else:
                print(f'O ', end='')
        print()
    print()


def under_attack(queens):
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False  # Ферзи бьют друг друга
    return True  # Ферзи не бьют друг друга


def generate_random_queens():
    queens = []
    choices = list(range(1, BOARD_SIZE + 1))
    for i in range(1, BOARD_SIZE + 1):
        # Генерируем уникальные случайные координаты для каждого ферзя
        x = i
        y = choices.pop(random.randrange(len(choices)))
        queens.append((x, y))
    return queens


__all__ = ['under_attack', 'print_board', 'generate_random_queens']

if __name__ == "__main__":
    test_qweens = [
        (1, 7), (2, 2), (3, 4), (4, 1), (5, 8), (6, 5), (7, 3), (8, 6)
    ]
    print(under_attack(test_qweens))  # True - не бьют друг друга
    lucky_qweens = []
    count = 0
    while len(lucky_qweens) < 4:
        queens = generate_random_queens()
        if under_attack(queens):
            lucky_qweens.append(queens)
        count += 1

    for i, qweens in enumerate(lucky_qweens, start=1):
        print(f"Успешная расстановка {i}: ")
        print(f"{qweens}")
        print_board(qweens)
        print()

    print(f"Всего попыток: {count}")
