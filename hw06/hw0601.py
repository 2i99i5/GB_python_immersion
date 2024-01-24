"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату
в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая
дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский
календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

2. В модуль с проверкой даты добавьте возможность запуска в терминале с
передачей даты на проверку.
"""
import calendar
import sys
import argparse
from datetime import datetime


def create_parser():
    parser = argparse.ArgumentParser(description='Check date availability ')
    parser.add_argument(
        '--date',
        type=str,
        default="29.02.2000",
        help='provide a string (default: 29.02.2000)'
    )
    return parser


def check_date(date_str: str) -> bool:
    try:
        day, month, year = [int(i) for i in date_str.split('.')]
    except:
        return False
    try:
        datetime(day=day, month=month, year=year)
        print(f"{'Високосный' if _check_leap(year) else 'Невисокосный'}")
        return True
    except:
        return False


def _check_leap(year: int) -> bool:
    if calendar.isleap(year):
        return True
    return False


__all__ = ['check_date']

if __name__ == "__main__":
    parser = create_parser()
    date = parser.parse_args(sys.argv[1:])
    print(check_date(date.date))
