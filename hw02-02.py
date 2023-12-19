# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

while True:
    dec_num = input("Введите целое число: ")
    if dec_num.isdigit():
        dec_num = int(dec_num)
        break
hex_str = hex(dec_num)

res = []
while dec_num > 0:
    digit = dec_num % 16
    match digit:
        case 10:
            digit = "a"
        case 11:
            digit = "b"
        case 12:
            digit = "c"
        case 13:
            digit = "d"
        case 14:
            digit = "e"
        case 15:
            digit = "f"
        case _:
            digit = str(digit)
    res.append(digit)
    dec_num //= 16
hex_num = ''.join(res[::-1])
print(hex_num)
print(hex_str)  # проверка
