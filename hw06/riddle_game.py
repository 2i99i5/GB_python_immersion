"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и
количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль,
если попытки исчерпаны.
"""


def guess_riddle(riddle, answers, right_num, count=3):
    total = 0
    while count != total:
        total += 1
        print(riddle)
        for i, answer in enumerate(answers, 1):
            print(f'{i}: {answer} ')
        user_input = int(input('Введите вариант ответа: '))
        if user_input == right_num:
            return total
    return 0


if __name__ == "__main__":
    print(guess_riddle(
        "Коричневое пушистое",
        ("стол", "стул", "кошка", "шар"),
        3,
        2))
