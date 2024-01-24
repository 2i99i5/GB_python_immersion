"""
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые
могут верно работать за пределами модуля.
"""
from .hw0601 import check_date
from .hw0602 import under_attack, print_board, generate_random_queens

# import .agr_riddle
#
# import .dict_riddle
# import .less_or_more
# import riddle_game

# __all__ = [
# less_or_more.game,
# riddle_game.guess_riddle,
# dict_riddle.riddle_dict,
# check_date,
# agr_riddle.agr_results,
# agr_riddle.print_results
# ]
__all__ = ['hw0601', 'hw0602']
