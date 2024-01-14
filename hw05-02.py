"""
3. Напишите однострочный генератор словаря, который принимает на вход три
списка одинаковой длины: имена str, ставка int, премия str с указанием
процентов вида “10.25%”. В результате получаем словарь с именем в качестве
ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
умноженная на процент премии
"""


def gen_dict(names: list[str], rates: list[int],
             bonuses: list[str]) -> dict[str:float]:
    return {names[i]: rates[i] * (float(bonuses[i][:-1]) / 100)
            for i in range(len(rates))}


def gen_dict_yield(names: list[str], rates: list[int],
                   bonuses: list[str]) -> dict[str:float]:
    yield {name: rate * bonus / 100 for name, rate, bonus in
           zip(names, rates, (float(bonus[:-1]) for bonus in bonuses))}


names = ['Volodya', 'Olya', 'Natalya']
rates = [50_000, 70_000, 35_000]
bonuses = ['12.5%', '10%', '15.1%']
print(gen_dict(names, rates, bonuses))
print(*gen_dict_yield(names, rates, bonuses))
