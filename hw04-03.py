# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег

# 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

MIN_DELTA = 50
ITER_CONST = 3
COMMISSION_PERCENT = 1.5
COMMISSION_MIN = 30
COMMISSION_MAX = 600
TAX_LIMIT = 5_000_000
TAX = 10
ITER_PERCENT = 3

log_list = []


def check_tax(balance):
    """
    Снятие налога на богатство.
    :param balance: float
    :return: float
    """
    if balance > TAX_LIMIT:
        return balance * (100 - TAX) / 100
    return balance


def get_percent(delta):
    """
    Рассчет суммы снятия
    :param delta: float
    :return: float
    """
    temp = delta * COMMISSION_PERCENT / 100
    if temp < COMMISSION_MIN:
        temp = COMMISSION_MIN
    if temp > COMMISSION_MAX:
        temp = COMMISSION_MAX
    return temp


def add_percent(balance):
    """
    Добавление процента за третью операцию
    :param balance: float
    :return: float
    """
    global log_list
    log_list.append(+(balance * ITER_PERCENT / 100))
    return balance * (1 + ITER_PERCENT / 100)


def add(balance, count_iter):
    """
    Пополнение баланса
    :param balance: float
    :param count_iter: float
    :return: tuple
    """
    while True:
        delta = input('Введите сумму пополнения: ')
        if delta.isdigit():
            delta = int(delta)
            if delta % MIN_DELTA != 0:
                print(f'Введите сумму, кратную {MIN_DELTA} рублей ')
            else:
                break
        else:
            print(f'Введите число: ')
    global log_list
    log_list.append(delta)
    balance += delta
    count_iter += 1
    if count_iter % ITER_CONST == 0:
        balance = add_percent(balance)
    return balance, count_iter


def get(balance, count_iter):
    """
    Снятие денег
    :param balance: float
    :param count_iter: int
    :return: tuple
    """
    while True:
        delta = input('Введите сумму снятия: ')
        if delta.isdigit():
            delta = int(delta)
            if delta % MIN_DELTA != 0:
                print(f'Введите сумму, кратную {MIN_DELTA} рублей ')
            else:
                temp = get_percent(delta)
                if temp + delta > balance:
                    print('Недостаточно денег на счете! ')
                else:
                    break
        else:
            print(f'Введите число: ')
    global log_list
    log_list.append(-(delta + temp))
    balance -= (delta + temp)
    count_iter += 1
    if count_iter % ITER_CONST == 0:
        balance = add_percent(balance)
    return balance, count_iter


def print_sum(balance):
    """
    Печать данных о балансе
    :param balance: float
    :return:
    """
    global log_list
    print(f'На Вашем счету {balance} рублей')
    print(f'{log_list}')


def menu():
    """
    Меню банкомата
    :return:
    """
    menu_text = """
    1 - Пополнить
    2 - Снять
    3 - Выйти
    """
    balance = 0
    count_iter = 0
    while True:
        print(menu_text)
        while True:
            user_input = input('Введите номер пункта: ')
            if user_input in ('1', '2', '3'):
                break
        match user_input:
            case "1":
                balance = check_tax(balance)
                balance, count_iter = add(balance, count_iter)
                print_sum(balance)
            case "2":
                balance = check_tax(balance)
                balance, count_iter = get(balance, count_iter)
                print_sum(balance)
            case "3":
                print_sum(balance)
                break
            case _:
                print('неверный ввод. ')


if __name__ == "__main__":
    menu()
