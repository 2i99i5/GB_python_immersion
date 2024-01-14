"""
4. Создайте функцию генератор чисел Фибоначчи
"""


def fib(n: int) -> list[int]:
    fib1, fib2 = 0, 1
    for _ in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


length = int(input("Введите длину списка чисел Фибоначчи: "))
print(*(fib(length)))
