# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за
# 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой
# попытки. Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
COUNT_LIMIT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
cnt = COUNT_LIMIT

print(f'Игра УГАЖДАЙ ЧИСЛО. Загадано число, у Вас {cnt} попыток, '
      f'чтобы его отгадать.')
# print(num)
while cnt > 0:
    answer = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}. '))
    cnt -= 1
    if answer > num:
        print(f'Меньше. У Вас осталось {cnt} попыток. ')
    elif answer < num:
        print(f'Больше. У Вас осталось {cnt} попыток. ')
    else:
        print(f'Победа! Вы угадали число {num} с {COUNT_LIMIT - cnt} попыток. ')
        break
else:
    print(f'Попытки закончились! Было загадано {num} ')
