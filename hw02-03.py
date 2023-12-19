# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction
from math import gcd


def reducing_fraction(fraction_list: list[int]) -> list[str]:
    # сокращает дробь
    nod = gcd(*fraction_list)  # вычисление НОД
    return [str(int(i / nod)) for i in fraction_list]


def print_fraction(fraction_list: list[str]) -> str:
    # выводит дробь в виде "a/b"
    return "/".join(fraction_list)


a = input("Введите дробь a: ")
b = input("Введите дробь b: ")
a_fraction = Fraction(a)
b_fraction = Fraction(b)
sum_fraction = a_fraction + b_fraction
multi_fraction = a_fraction * b_fraction
print(f'{sum_fraction=}\t{multi_fraction=}')  # проверочный с Fraction

lst_a = a.split('/', 1)
lst_a = list(map(int, lst_a))
lst_b = b.split('/', 1)
lst_b = list(map(int, lst_b))

sum_numerator = lst_a[0] * lst_b[1] + lst_b[0] * lst_a[1]
sum_denominator = lst_a[1] * lst_b[1]
sum_fraction = []
sum_fraction.append(sum_numerator)
sum_fraction.append(sum_denominator)
sum_fraction = reducing_fraction(sum_fraction)
print(f'Сумма дробей = {print_fraction(sum_fraction)}')

multi_fraction = [x * y for x, y in zip(lst_a, lst_b)]
multi_fraction = reducing_fraction(multi_fraction)
print(f'Произведение дробей = {print_fraction(multi_fraction)}')
